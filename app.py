import streamlit as st
from groq import Groq

# 1. Page Configuration (Optional für ein schöneres UI)
st.set_page_config(page_title="Meine KI, meine Stimme?", page_icon="🤖")

# 2. Groq Client initialisieren
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

# 3. Seitenleiste (Sidebar) mit Reset-Button
with st.sidebar:
    st.header("Einstellungen")
    st.write("Verwalten Sie hier den Verlauf Ihrer Diskussion.")
    if st.button("🗑️ Chatverlauf zurücksetzen", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 4. Hauptansicht
st.title("Meine KI, meine Stimme?")

# Chatverlauf initialisieren
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bisherige Nachrichten anzeigen
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Benutzereingabe verarbeiten
if prompt := st.chat_input("Eure Frage zu einer lokalen Entscheidung"):
    # Nutzernachricht speichern und anzeigen
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Nachricht an Groq senden
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

    # Assistenten-Antwort speichern und anzeigen
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
