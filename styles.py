import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* ================================
       GLOBAL
    ================================= */

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(45, 85, 180, 0.18), transparent 35%),
            linear-gradient(135deg, #07111f 0%, #0b1628 50%, #101c33 100%);
    }

    .main {
        padding-top: 1rem;
    }

    h1 {
        font-size: 2.4rem !important;
        font-weight: 750 !important;
        letter-spacing: -1px;
    }

    h2 {
        font-weight: 700 !important;
    }

    h3 {
        font-weight: 650 !important;
    }

    /* ================================
       SIDEBAR
    ================================= */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #07101e 0%, #0c1728 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] h3 {
        color: #ffffff;
        line-height: 1.35;
    }

    [data-testid="stSidebar"] .stRadio label {
        padding: 10px 12px;
        border-radius: 10px;
        margin-bottom: 4px;
    }

    /* ================================
       HERO
    ================================= */

    .hero {
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(30, 70, 150, 0.55),
                rgba(80, 45, 150, 0.35)
            );

        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        color: #b9c7e6;
        font-size: 1.05rem;
    }

    /* ================================
       CARDS
    ================================= */

    .card {
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        backdrop-filter: blur(12px);
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .card-text {
        color: #aebbd5;
        line-height: 1.6;
    }

    /* ================================
       FEATURE CARDS
    ================================= */

    .feature {
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        min-height: 145px;
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }

    .feature-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: white;
    }

    .feature-text {
        color: #aab8d1;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    /* ================================
       STATUS BADGES
    ================================= */

    .status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 6px;
    }

    .status-green {
        background: rgba(40, 200, 120, 0.15);
        color: #55e39b;
        border: 1px solid rgba(40,200,120,0.25);
    }

    .status-yellow {
        background: rgba(255,190,60,0.15);
        color: #ffd166;
        border: 1px solid rgba(255,190,60,0.25);
    }

    /* ================================
       METRICS
    ================================= */

    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    [data-testid="stMetricLabel"] {
        color: #9eacc8 !important;
    }

    [data-testid="stMetricValue"] {
        color: white !important;
        font-weight: 750 !important;
    }

    /* ================================
       BUTTONS
    ================================= */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.12);
        font-weight: 650;
        min-height: 42px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        border-color: rgba(100,150,255,0.5);
    }

    /* ================================
       FILE UPLOADER
    ================================= */

    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.035);
        border: 1px dashed rgba(120,160,255,0.35);
        border-radius: 15px;
        padding: 10px;
    }

    /* ================================
       INPUTS
    ================================= */

    .stTextInput input,
    .stTextArea textarea {
        border-radius: 10px;
        background: rgba(255,255,255,0.045);
    }

    /* ================================
       EXPANDER
    ================================= */

    [data-testid="stExpander"] {
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        background: rgba(255,255,255,0.035);
    }

    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        padding: 30px 10px 10px;
        color: #71809d;
        font-size: 0.8rem;
    }

    </style>
    """, unsafe_allow_html=True)