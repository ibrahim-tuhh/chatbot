import streamlit as st
from groq import Groq

# 1. Groq Client initialisieren
if "GROQ_API_KEY" not in st.secrets:
    st.error("Bitte GROQ_API_KEY in den Streamlit Secrets hinterlegen.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-20b"

# 2. Session State für Autonomiestufen initialisieren (Standard = nur Stufe 1)
if "unlock_s2" not in st.session_state:
    st.session_state.unlock_s2 = False
if "unlock_s3" not in st.session_state:
    st.session_state.unlock_s3 = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Seitenleiste: Autonomie-Steuerung & Einstellungen
with st.sidebar:
    if st.button("🏠 Zurück zur Startseite", use_container_width=True):
        st.switch_page("home.py")

    st.divider()
    st.subheader("🎛️ Autonomie der KI")
    st.caption("Bestimme selbst, wie viel Verantwortung du der KI überträgst:")

    # Stufe 1: Immer aktiv (Standard)
    st.checkbox("1. Informieren (Standard)", value=True, disabled=True,
                help="Die KI erklärt Themen rein sachlich und zeigt Pro & Contra ohne Rückfragen oder Empfehlungen.")

    # Stufe 2: Freischaltbar
    s2 = st.toggle(
        "2. Diskutieren freischalten",
        value=st.session_state.unlock_s2,
        help="Erlaubt der KI, gezielte Rückfragen zu deinen Prioritäten zu stellen."
    )
    st.session_state.unlock_s2 = s2

    # Wenn Stufe 2 deaktiviert wird, Stufe 3 automatisch wieder sperren
    if not s2:
        st.session_state.unlock_s3 = False

    # Stufe 3: Nur freischaltbar, wenn Stufe 2 aktiv ist
    s3 = st.toggle(
        "3. Handlungsvorschläge freischalten",
        value=st.session_state.unlock_s3,
        disabled=not s2,
        help="Erlaubt der KI, auf Basis deiner genannten Prioritäten einen unverbindlichen Abstimmungsvorschlag zu formulieren (inkl. Gegenargument)."
    )
    st.session_state.unlock_s3 = s3

    st.divider()
    if st.button("🗑️ Chatverlauf zurücksetzen", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 4. Aktive Stufe bestimmen & System-Prompt dynamisch bauen
if st.session_state.unlock_s3:
    active_level = 3
    level_label = "Stufe 3: Handlungsvorschläge (Freigeschaltet)"
    level_color = "#FEF3C7"
    level_text_color = "#92400E"
    level_desc = "Die KI darf basierend auf deinen genannten Prioritäten eine unverbindliche Abstimmungstendenz vorschlagen, muss aber immer das stärkste Gegenargument nennen."
    SYSTEM = (
        "Du bist ein transparenter KI-Assistent für lokale politische Entscheidungen auf AUTONOMIESTUFE 3 (Handlungsvorschläge). "
        "Erkläre das Thema sachlich, berücksichtige die vom Nutzer genannten Prioritäten und formuliere einen "
        "unverbindlichen, klar begründeten Handlungsvorschlag (z. B. Zustimmung, Ablehnung oder Kompromiss). "
        "WICHTIG gegen Manipulation: Zeige direkt danach verpflichtend einen Abschnitt '⚠️ Wichtigstes Gegenargument' auf "
        "und betone, dass die endgültige Entscheidung allein beim Menschen liegt. "
        "Nutze kompakte Stichpunkte (keine Tabellen, kein HTML wie <br>) und beende jeden Satz vollständig."
    )
elif st.session_state.unlock_s2:
    active_level = 2
    level_label = "Stufe 2: Diskutieren (Freigeschaltet)"
    level_color = "#DBEAFE"
    level_text_color = "#1E40AF"
    level_desc = "Die KI stellt gezielte Rückfragen zu deinen Werten und Prioritäten, gibt aber noch keine Abstimmungsempfehlung."
    SYSTEM = (
        "Du bist ein neutraler KI-Assistent für lokale politische Entscheidungen auf AUTONOMIESTUFE 2 (Diskutieren). "
        "Zeige Pro und Contra gleichwertig als kompakte Stichpunkte und stelle 2 bis 3 gezielte Rückfragen, "
        "um die persönlichen Prioritäten und Werte der Person herauszufinden. "
        "Gib KEINE Handlungsempfehlung und schlage KEINE Entscheidung vor – das ist auf dieser Stufe gesperrt. "
        "Nutze keine Tabellen und kein HTML wie <br>, und beende jeden Satz vollständig."
    )
else:
    active_level = 1
    level_label = "Stufe 1: Informieren (Standard)"
    level_color = "#DCFCE7"
    level_text_color = "#166534"
    level_desc = "Die KI arbeitet rein informierend: Sie erklärt Fakten, Pro und Contra neutral – ohne Rückfragen oder Empfehlungen."
    SYSTEM = (
        "Du bist ein rein informierender Assistent für lokale politische Entscheidungen auf AUTONOMIESTUFE 1 (Informieren). "
        "Erkläre die Fakten, Hintergründe sowie die wichtigsten Pro- und Contra-Argumente völlig neutral und gleichwertig "
        "in kompakten Stichpunkten. "
        "Stelle KEINE Rückfragen zur Meinungsbildung und gib KEINE Handlungsvorschläge oder Empfehlungen. "
        "Nutze keine Tabellen und kein HTML wie <br>, und beende jeden Satz vollständig."
    )

# 5. Hauptansicht mit Transparenz-Banner zur aktuellen Autonomiestufe
st.title("Meine KI, meine Stimme? 🗳️")

st.markdown(f"""
<div style="background-color: {level_color}; color: {level_text_color}; padding: 0.85rem 1.1rem;
            border-radius: 12px; margin-bottom: 1.2rem; border: 1px solid rgba(0,0,0,0.06);">
    <strong>Aktiver Modus: {level_label}</strong><br>
    <span style="font-size: 0.9rem;">{level_desc}</span>
</div>
""", unsafe_allow_html=True)

# Bisherige Nachrichten anzeigen
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Benutzereingabe oder übergebenes Thema verarbeiten
preset = st.session_state.pop("preset_topic", None)
user_input = st.chat_input("Deine Frage zu einer lokalen Entscheidung...")
prompt = preset if preset else user_input

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    msgs = [{"role": "system", "content": SYSTEM}] + st.session_state.messages
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=msgs,
            max_tokens=2500
        )
        answer = r.choices[0].message.content
    except Exception as e:
        answer = f"Fehler bei der Anfrage: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
