import streamlit as st

st.set_page_config(
    page_title="Meine KI, meine Stimme?",
    page_icon="🗳️",
    layout="wide"
)

# Alle Dateien liegen direkt im selben Verzeichnis (kein "pages/"-Präfix)
home_page = st.Page("home.py", title="Startseite", icon="🏠", default=True)
entscheidungen_page = st.Page("entscheidungen.py", title="Entscheidungen vor Ort", icon="📋")
chatbot_page = st.Page("chatbot.py", title="KI-Diskussionspartner", icon="🤖")

pg = st.navigation([home_page, entscheidungen_page, chatbot_page], position="hidden")
pg.run()
