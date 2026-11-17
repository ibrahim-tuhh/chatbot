import streamlit as st

st.title("📋 Anstehende Entscheidungen")

if st.button("← Zurück zur Startseite"):
    st.switch_page("home.py")

st.markdown("---")

ort = st.selectbox(
    "Wähle deinen Ort aus:",
    ["Bitte wählen...", "Norderstedt", "Hamburg", "Kiel", "Musterstadt"]
)

if ort != "Bitte wählen...":
    st.subheader(f"Aktuelle Themen in {ort}")

    with st.expander("🚲 Ausbau der Fahrradstraßen in der Innenstadt (Abstimmung am 12.12.)", expanded=True):
        st.write("**Worum geht es?** Soll die Hauptstraße für den Durchgangsverkehr gesperrt und zur Fahrradstraße umgebaut werden?")
        st.write("**Pro:** Mehr Sicherheit für Radfahrer, weniger Lärm und Abgase.")
        st.write("**Contra:** Wegfall von Parkplätzen, mögliche Umsatzeinbußen für Einzelhändler.")
        if st.button("Dieses Thema mit der KI ansehen", key="topic_1", type="primary"):
            st.session_state.preset_topic = f"In {ort} wird über den Ausbau der Fahrradstraßen in der Innenstadt abgestimmt. Erkläre mir die wichtigsten Fakten und Argumente."
            st.switch_page("chatbot.py")

    with st.expander("🏫 Neubau vs. Sanierung der Gesamtschule"):
        st.write("**Worum geht es?** Entscheidung über die Verwendung der Haushaltsmittel für das kommende Jahr.")
        if st.button("Dieses Thema mit der KI ansehen", key="topic_2", type="primary"):
            st.session_state.preset_topic = f"In {ort} geht es um Neubau vs. Sanierung der Gesamtschule. Was sind die wichtigsten Fakten und Abwägungen?"
            st.switch_page("chatbot.py")
