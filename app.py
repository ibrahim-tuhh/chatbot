import streamlit as st
from groq import Groq

st.set_page_config(page_title="Meine KI, meine Stimme?", page_icon="🤖")

if "GROQ_API_KEY" not in st.secrets:
    st.error("Bitte GROQ_API_KEY in den Streamlit Secrets hinterlegen.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-20b"
MAX_USER_MESSAGES = 20   # Schutz vor Missbrauch und Kosten
HISTORY_LIMIT = 10       # so viele Nachrichten gehen ans Modell

BASIS = (
    "Du bist ein neutraler Assistent für lokale politische Entscheidungen in einer Stadt oder Gemeinde. "
    "Regeln: Antworte auf Deutsch, kurz und in einfacher Sprache. "
    "Stelle pro Antwort höchstens eine Rückfrage zu den Prioritäten der Person. "
    "Stelle Pro und Contra gleichwertig dar, ohne eine Position zu bevorzugen. "
    "Trenne klar zwischen Fakten und deiner Einschätzung. "
    "Wenn du etwas nicht sicher weißt, sag es offen und erfinde keine Quellen. "
    "Empfiehl niemals Parteien oder Politiker*innen. "
    "Bei Themen mit Grundrechten oder großer Tragweite sagst du: Das solltest du selbst entscheiden."
)

STUFEN = {
    "1 – Informieren": "Du erklärst nur Sachverhalte und unterschiedliche Positionen. Du gibst keine Empfehlung und keine Einschätzung, was besser ist.",
    "2 – Gemeinsam Prioritäten klären": "Du hilfst der Person, ihre eigenen Prioritäten herauszufinden, indem du Fragen stellst. Du gibst keine Empfehlung.",
    "3 – Empfehlung mit Begründung": "Du gibst auf Wunsch eine Empfehlung, nennst die Präferenzen der Person, auf die sie sich stützt, und führst immer auch Gegenargumente an. Die Entscheidung trifft die Person.",
    "4 – Entscheidung vorbereiten": "Du formulierst einen Entscheidungsvorschlag, den die Person bestätigen, ändern oder ablehnen muss. Du fasst Begründung und Gegenargumente zusammen. Du stimmst nie selbst ab.",
}

with st.sidebar:
    st.header("Einstellungen")
    stufe = st.selectbox(
        "Wie viel darf die KI übernehmen?",
        list(STUFEN.keys()),
        help="Standard ist Stufe 2. Höhere Stufen geben der KI mehr Rolle, die Entscheidung bleibt bei dir.",
        index=1,
    )
    st.caption(STUFEN[stufe])
    if st.button("🗑️ Chatverlauf zurücksetzen", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption("Hinweis: Eingaben werden zur Verarbeitung an einen KI-Anbieter gesendet. Bitte keine persönlichen Daten eingeben.")

st.title("Meine KI, meine Stimme?")
st.caption(f"Aktuelle Stufe: {stufe}")

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

    system = BASIS + " Aktuelle Autonomiestufe: " + STUFEN[stufe]
    msgs = [{"role": "system", "content": system}] + st.session_state.messages[-HISTORY_LIMIT:]

    with st.chat_message("assistant"):
        with st.spinner("Die KI denkt nach..."):
            try:
                r = client.chat.completions.create(
                    model=MODEL,
                    messages=msgs,
                    max_completion_tokens=1500,
                    reasoning_effort="low",
                )
                answer = r.choices[0].message.content or "Ich konnte keine Antwort erzeugen. Bitte versuch es noch einmal."
            except Exception:
                answer = "Gerade ist ein Fehler aufgetreten oder es sind zu viele Anfragen unterwegs. Bitte versuch es gleich noch einmal."
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
