import streamlit as st

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        max-width: 960px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    .hero-badge {
        display: inline-block;
        background-color: #DBEAFE;
        color: #1E40AF;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.15;
        margin-bottom: 1rem;
        text-align: center;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #475569;
        max-width: 650px;
        margin: 0 auto 2.5rem auto;
        text-align: center;
        line-height: 1.6;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        height: 100%;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.12);
        border-color: #93C5FD !important;
    }
    .icon-box {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .icon-blue { background-color: #EFF6FF; }
    .icon-indigo { background-color: #EEF2FF; }
    .card-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.5rem;
    }
    .card-text {
        font-size: 0.98rem;
        color: #64748B;
        line-height: 1.55;
        min-height: 85px;
        margin-bottom: 1.2rem;
    }
    .stButton > button {
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center;">
    <span class="hero-badge">Neutral • Transparent • Lokal</span>
</div>
<h1 class="hero-title">Meine KI, meine Stimme?</h1>
<p class="hero-subtitle">
    Informiere dich unabhängig über anstehende Abstimmungen in deiner Gemeinde 
    und steuere selbst, wie viel Unterstützung deine KI übernimmt.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("""
            <div class="icon-box icon-blue">📋</div>
            <div class="card-title">Entscheidungen vor Ort</div>
            <div class="card-text">
                Sieh dir eine übersichtliche Zusammenfassung anstehender Bürgerentscheide, 
                Bauprojekte und Ratsthemen in deinem Ort an.
            </div>
        """, unsafe_allow_html=True)
        if st.button("Zur Übersicht →", use_container_width=True, type="primary"):
            st.switch_page("entscheidungen.py")

with col2:
    with st.container(border=True):
        st.markdown("""
            <div class="icon-box icon-indigo">💬</div>
            <div class="card-title">Mit dem Chatbot sprechen</div>
            <div class="card-text">
                Starte im reinen Informationsmodus und schalte bei Bedarf Diskussion 
                oder Handlungsvorschläge kontrolliert frei.
            </div>
        """, unsafe_allow_html=True)
        if st.button("Chat starten →", use_container_width=True, type="primary"):
            st.switch_page("chatbot.py")

st.markdown("""
<p style="text-align: center; color: #94A3B8; font-size: 0.85rem; margin-top: 3rem;">
    🔒 Standardmäßig arbeitet die KI rein informierend. Erweiterte Stufen müssen aktiv freigeschaltet werden.
</p>
""", unsafe_allow_html=True)
