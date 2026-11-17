import streamlit as st

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        max-width: 960px;
        padding-top: 3rem;
        padding-bottom: 4rem;
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

    /* Trust & Vergleichs-Sektion unten */
    .trust-section {
        margin-top: 4.5rem;
        padding-top: 3rem;
        border-top: 1px solid #E2E8F0;
    }
    .section-eyebrow {
        text-align: center;
        color: #2563EB;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.4rem;
    }
    .section-heading {
        text-align: center;
        font-size: 1.9rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0.7rem;
    }
    .section-sub {
        text-align: center;
        color: #475569;
        font-size: 1.05rem;
        max-width: 640px;
        margin: 0 auto 2.5rem auto;
        line-height: 1.6;
    }
    .pillar-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.4rem;
        height: 100%;
    }
    .pillar-icon {
        font-size: 1.4rem;
        margin-bottom: 0.6rem;
    }
    .pillar-title {
        font-weight: 700;
        font-size: 1.05rem;
        color: #0F172A;
        margin-bottom: 0.4rem;
    }
    .pillar-desc {
        font-size: 0.92rem;
        color: #64748B;
        line-height: 1.55;
    }
    .compare-box {
        background-color: #F1F5F9;
        border-radius: 16px;
        padding: 1.8rem;
        margin-top: 2rem;
        border: 1px solid #E2E8F0;
    }
    .compare-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    .compare-col-bad {
        background: #FFFFFF;
        padding: 1.3rem;
        border-radius: 12px;
        border-left: 4px solid #CBD5E1;
    }
    .compare-col-good {
        background: #FFFFFF;
        padding: 1.3rem;
        border-radius: 12px;
        border-left: 4px solid #2563EB;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.08);
    }
    .compare-header {
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 0.8rem;
        color: #0F172A;
    }
    .compare-list {
        list-style: none;
        padding: 0;
        margin: 0;
        font-size: 0.92rem;
        color: #475569;
        line-height: 1.7;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HERO BEREICH ---
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

# --- 2. AUSWAHL-KARTEN ---
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

# --- 3. TRUST & DIFFERENZIERUNGS-SEKTION ("WARUM UNS VERTRAUEN?") ---
st.markdown("""
<div class="trust-section">
    <div class="section-eyebrow">Kooperative Intelligenz statt Blackbox</div>
    <h2 class="section-heading">Warum dieses System anders arbeitet als herkömmliche KI</h2>
    <p class="section-sub">
        Gängige Sprachmodelle (LLMs) sind darauf trainiert, möglichst gefällig zu antworten oder 
        vorschnelle Empfehlungen abzugeben. Unsere Architektur schützt deine freie Meinungsbildung.
    </p>
</div>
""", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3, gap="medium")

with p1:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-icon">🎚️</div>
        <div class="pillar-title">Gestaffelte Autonomie</div>
        <div class="pillar-desc">
            Du behältst die Kontrolle: Standardmäßig liefert die KI nur neutrale Fakten (Stufe 1). 
            Diskussion und Vorschläge müssen von dir aktiv freigeschaltet werden.
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-icon">⚖️</div>
        <div class="pillar-title">Anti-Influencer-Prinzip</div>
        <div class="pillar-desc">
            Keine versteckte Beeinflussung: Jedes Thema wird ausgewogen beleuchtet – und selbst bei 
            freigeschalteten Vorschlägen zeigt die KI zwingend das stärkste Gegenargument.
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-icon">🧭</div>
        <div class="pillar-title">Mensch bleibt Entscheider</div>
        <div class="pillar-desc">
            Nach dem Prinzip der Kooperativen Intelligenz ersetzt unsere KI deine Stimme nicht, 
            sondern strukturiert Informationen so, dass du souverän selbst entscheidest.
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. DIREKTVERGLEICH: HERKÖMMLICHE LLMS VS. UNSERE KI ---
st.markdown("""
<div class="compare-box">
    <div class="compare-grid">
        <div class="compare-col-bad">
            <div class="compare-header">❌ Herkömmliche Chatbots (Standard-LLMs)</div>
            <ul class="compare-list">
                <li>• Neigen zu einseitigen Antworten, je nach Fragestellung</li>
                <li>• Vermischen Fakten, Rückfragen und Meinungen unkontrolliert</li>
                <li>• Intransparente Rolle: Unklar, wie stark die KI gerade lenkt</li>
                <li>• Optimiert auf schnelle Zustimmung statt kritische Abwägung</li>
            </ul>
        </div>
        <div class="compare-col-good">
            <div class="compare-header">✅ Meine KI, meine Stimme?</div>
            <ul class="compare-list">
                <li>• <strong>Strikte Rollentrennung:</strong> 3 klar abgegrenzte Autonomiestufen</li>
                <li>• <strong>Sichtbarer Modus:</strong> Jederzeit erkennbar, was die KI gerade darf</li>
                <li>• <strong>Pflicht zur Gegenseite:</strong> Pro &amp; Contra immer gleichwertig</li>
                <li>• <strong>Lokal &amp; zweckgebunden:</strong> Fokus auf kommunale Entscheidungen</li>
            </ul>
        </div>
    </div>
</div>

<p style="text-align: center; color: #94A3B8; font-size: 0.85rem; margin-top: 2.5rem;">
    🔒 Entwickelt für transparente demokratische Teilhabe – keine Wahlempfehlungen, keine versteckte Steuerung.
</p>
""", unsafe_allow_html=True)
