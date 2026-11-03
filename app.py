import streamlit as st
from groq import Groq

# 1. Groq als API-Anbieter initialisieren
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 2. Ein aktives Modell wählen, das auf Groq läuft
MODEL = "llama-3.3-70b-versatile"

SYSTEM = (
    "Du bist ein neutraler Assistent für lokale politische Entscheidungen. "
    "Stelle Rückfragen zu Prioritäten, zeige Pro und Contra gleichwertig, "
    "empfiehl keine Parteien und überlasse die Entscheidung der Person."
)

st.title("Meine KI, meine Stimme?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Eure Frage zu einer lokalen Entscheidung"):
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
        answer = f"Fehler: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
