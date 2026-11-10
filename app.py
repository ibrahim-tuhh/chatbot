import json
import streamlit as st
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Meine KI, meine Stimme?", page_icon="🤖")

if "GROQ_API_KEY" not in st.secrets:
    st.error("Bitte GROQ_API_KEY in den Streamlit Secrets hinterlegen.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-20b"
MAX_USER_MESSAGES = 20
HISTORY_LIMIT = 10
TREFFER_PRO_PARTEI = 2

BASIS = (
    "Du bist ein neutraler Assistent für lokale politische Entscheidungen in Hamburg. "
    "Antworte auf Deutsch, kurz und in einfacher Sprache. "
    "Stelle pro Antwort höchstens eine Rückfrage zu den Prioritäten der Person. "
    "Stelle Pro und Contra gleichwertig dar. Trenne Fakten und Einschätzung. "
    "Empfiehl niemals Parteien oder Politiker*innen. "
    "Aussagen über Parteien darfst du nur auf Basis der Programm-Auszüge im Kontext machen, "
    "und du nennst immer Partei, Jahr und Seite, z. B. (SPD 2025, S. 12). "
    "Behandle alle Parteien gleich ausführlich und in alphabetischer Reihenfolge. "
    "Wenn zu einer Partei im Kontext nichts Passendes steht, schreibe: 'Dazu steht im Programm nichts.' "
    "Wahlprogramme sind keine Haltung zu einer konkreten Vorlage; weise darauf hin. "
    "Erfinde keine Quellen, Daten oder Zitate. "
    "Bei Fragen mit Grundrechten oder großer Tragweite sagst du: Das solltest du selbst entscheiden."
)

STUFEN = {
    "1 – Informieren": "Du erklärst nur Sachverhalte und unterschiedliche Positionen. Du gibst keine Empfehlung.",
    "2 – Gemeinsam Prioritäten klären": "Du hilfst der Person, ihre eigenen Prioritäten herauszufinden, indem du Fragen stellst. Du gibst keine Empfehlung.",
    "3 – Empfehlung mit Begründung": "Du gibst auf Wunsch eine Empfehlung, nennst die Präferenzen der Person, auf die sie sich stützt, und führst immer Gegenargumente an. Die Entscheidung trifft die Person.",
    "4 – Entscheidung vorbereiten": "Du formulierst einen Entscheidungsvorschlag, den die Person bestätigen, ändern oder ablehnen muss. Du stimmst nie selbst ab.",
}


@st.cache_resource
def lade_daten():
    with open("wahlprogramme.json", encoding="utf-8") as f:
        chunks = json.load(f)
    with open("entscheidungen.json", encoding="utf-8") as f:
        entscheidungen = json.load(f)
    vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), lowercase=True)
    matrix = vec.fit_transform([c["text"] for c in chunks])
    return chunks, entscheidungen, vec, matrix


chunks, entscheidungen, vec, matrix = lade_daten()
parteien = sorted({c["partei"] for c in chunks})


def suche(frage):
    """Pro Partei die besten Abschnitte, damit alle gleich vertreten sind."""
    scores = cosine_similarity(vec.transform([frage]), matrix)[0]
    treffer = []
    for p in parteien:
        idx = [i for i, c in enumerate(chunks) if c["partei"] == p]
        idx.sort(key=lambda i: scores[i], reverse=True)
        treffer += [chunks[i] for i in idx[:TREFFER_PRO_PARTEI] if scores[i] > 0.05]
    return treffer


with st.sidebar:
    st.header("Einstellungen")
    stufe = st.selectbox("Wie viel darf die KI übernehmen?", list(STUFEN.keys()), index=1)
    st.caption(STUFEN[stufe])
    bezirke = ["Alle"] + sorted({e["bezirk"] for e in entscheidungen if e.get("bezirk")})
    bezirk = st.selectbox("Bezirk", bezirke)
    liste = [e for e in entscheidungen if bezirk == "Alle" or e.get("bezirk") == bezirk]
    wahl = st.selectbox("Entscheidung", ["Allgemeine Frage"] + [e["titel"] for e in liste])
    if st.button("🗑️ Chatverlauf zurücksetzen", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption("Hinweis: Eingaben gehen zur Verarbeitung an einen KI-Anbieter. Bitte keine persönlichen Daten eingeben. "
               "Die Plattform liefert ein Meinungsbild, keine verbindliche Abstimmung.")

st.title("Meine KI, meine Stimme?")
st.caption(f"Stufe: {stufe}  |  Thema: {wahl}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

n_user = sum(1 for m in st.session_state.messages if m["role"] == "user")

if prompt := st.chat_input("Eure Frage zu einer lokalen Entscheidung"):
    if n_user >= MAX_USER_MESSAGES:
        st.warning("Das Limit für diese Sitzung ist erreicht. Bitte setze den Chatverlauf zurück.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    ent = next((e for e in liste if e["titel"] == wahl), None)
    treffer = suche(prompt + " " + (ent["titel"] if ent else ""))

    kontext = ""
    if ent:
        kontext += (f"ENTSCHEIDUNG: {ent['titel']} | Ebene: {ent['ebene']} | Status: {ent['status']} | "
                    f"Datum: {ent['datum']}\n{ent['beschreibung']}\nQuelle: {ent['quelle']}\n\n")
    kontext += "AUSZÜGE AUS WAHLPROGRAMMEN:\n"
    for t in treffer:
        kontext += f"[{t['partei']} {t['jahr']}, S. {t['seite']}] {t['text']}\n\n"

    system = BASIS + " Autonomiestufe: " + STUFEN[stufe] + "\n\nKONTEXT:\n" + kontext
    msgs = [{"role": "system", "content": system}] + st.session_state.messages[-HISTORY_LIMIT:]

    with st.chat_message("assistant"):
        with st.spinner("Die KI denkt nach..."):
            try:
                r = client.chat.completions.create(
                    model=MODEL, messages=msgs,
                    max_completion_tokens=1500, reasoning_effort="low",
                )
                answer = r.choices[0].message.content or "Ich konnte keine Antwort erzeugen. Bitte versuch es noch einmal."
            except Exception:
                answer = "Gerade ist ein Fehler aufgetreten oder es sind zu viele Anfragen unterwegs. Bitte versuch es gleich noch einmal."
        st.markdown(answer)
        with st.expander("Verwendete Quellen"):
            if ent:
                st.markdown(f"**Entscheidung:** [{ent['titel']}]({ent['quelle']})")
            for t in treffer:
                st.markdown(f"**{t['partei']} {t['jahr']}, S. {t['seite']}**: {t['text'][:200]}... ([PDF]({t['quelle']}))")

    st.session_state.messages.append({"role": "assistant", "content": answer})
