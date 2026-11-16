import streamlit as st

st.title("Meine KI, meine Stimme? 🗳️")
st.subheader("Informiere dich neutral und bilde dir deine eigene Meinung zu lokalen Themen.")

st.write("Wie möchtest du starten?")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 📋 Entscheidungen vor Ort")
        st.write(
            "Sieh dir eine Übersicht anstehender demokratischer Entscheidungen, "
            "Bürgerentscheide oder Ratsthemen in deinem Ort an."
        )
        if st.button("Zur Übersicht", use_container_width=True, type="primary"):
            st.switch_page("pages/entscheidungen.py")

with col2:
    with st.container(border=True):
        st.markdown("### 🤖 Mit dem Chatbot sprechen")
        st.write(
            "Diskutiere ein Thema deiner Wahl. Die KI zeigt dir Pro und Contra "
            "und hilft dir, deine eigenen Prioritäten abzuwägen."
        )
        if st.button("Chat starten", use_container_width=True, type="primary"):
            st.switch_page("pages/chatbot.py")
