import streamlit as st
from groq import Groq

# 1. Groq Client initialisieren
if "GROQ_API_KEY" not in st.secrets:
    st.error("Bitte GROQ_API_KEY in den Streamlit Secrets hinterlegen.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-20b"
SYSTEM = (
    "Du bist ein neutraler Assistent für lokale politische Entscheidungen. "
    "Stelle Rückfragen zu Prioritäten, zeige Pro und Contra gleichwertig, "
    "empfiehl keine Parteien und überlasse die Entscheidung der Person."
)

# 2. Seitenleiste (Sidebar) mit Reset- und Zurück-Button
with st.sidebar:
    if st.button("🏠 Zurück zur Startseite", use_container_width=True):
        st.switch_page("home.py")
    st.divider()
    st.header("Einstellungen")
    st.write("Verwalten Sie hier den Verlauf Ihrer Diskussion.")
    if st.button("🗑️ Chatverlauf zurücksetzen", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 3. Hauptansicht
st.title("Meine KI, meine Stimme?")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Bisherige Nachrichten anzeigen
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Prüfen, ob ein Thema von der Entscheidungs-Seite übergeben wurde, oder normale Eingabe nutzen
preset = st.session_state.pop("preset_topic", None)
user_input = st.chat_input("Eure Frage zu einer lokalen Entscheidung")
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
            max_tokens=500
        )
        answer = r.choices[0].message.content
    except Exception as e:
        answer = f"Fehler bei der Anfrage: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
