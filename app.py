import streamlit as st

st.set_page_config(page_title="Meine KI, meine Stimme?", page_icon="🗳️", layout="centered")

# Seiten definieren
home_page = st.Page("home.py", title="Startseite", icon="🏠", default=True)
entscheidungen_page = st.Page("entscheidungen.py", title="Entscheidungen vor Ort", icon="📋")
chatbot_page = st.Page("chatbot.py", title="KI-Diskussionspartner", icon="🤖")

# Navigation einrichten
pg = st.navigation([home_page, entscheidungen_page, chatbot_page])
pg.run()
