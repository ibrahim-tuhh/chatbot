import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(api_key=st.secrets["HF_TOKEN"])
MODEL = "MODELLNAME"  # auf der Hugging-Face-Modellseite kopieren

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
        r = client.chat_completion(model=MODEL, messages=msgs, max_tokens=500)
        answer = r.choices[0].message.content
    except Exception as e:
        answer = f"Fehler: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
