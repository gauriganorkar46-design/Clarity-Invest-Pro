# =========================================================
# GLOBAL STYLES
# =========================================================

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ======================================================
IMPORT FONT
====================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');


/* ======================================================
GLOBAL APP
====================================================== */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}


/* ======================================================
APP BACKGROUND
====================================================== */

.stApp {
    background: linear-gradient(135deg,#020617,#071127,#0F172A);
    color: white;
}


/* ======================================================
TEXT (UNIFIED SYSTEM)
====================================================== */

/* Paragraphs */

p {

    color: #D1D5DB !important;

    font-size: 23px !important;

    line-height: 1.9 !important;

    font-weight: 400;
}

/* Lists */

li {

    color: #D1D5DB !important;

    font-size: 23px !important;

    line-height: 1.9 !important;

    margin-bottom: 8px;
}

/* Labels */

label {

    color: #E5E7EB !important;

    font-size: 22px !important;

    font-weight: 600 !important;
}

/* Generic Span */

span {

    font-size: 22px;
}

/* ======================================================
MAIN CONTAINER
====================================================== */

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 1.2rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 1600px;
}


/* ======================================================
SIDEBAR
====================================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#020617,#0F172A);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}


/* ======================================================
HEADINGS
====================================================== */

h1 {

    color: white !important;

    font-size: 4.2rem !important;

    font-weight: 800 !important;

    letter-spacing: -1px;

    line-height: 1.2;
}

/* Section Heading */

h2 {

    color: white !important;

    font-size: 3.8rem !important;

    font-weight: 700 !important;

    line-height: 1.3;
}

/* Card / Sub Heading */

h3 {

    color: white !important;

    font-size: 2.5rem !important;

    font-weight: 700 !important;

    line-height: 1.4;
}

/* ======================================================
STREAMLIT TITLES
====================================================== */

.stTitle {

    font-size: 4.2rem !important;

    font-weight: 800 !important;
}

.stMarkdown h1 {

    font-size: 4.2rem !important;
}

.stMarkdown h2 {

    font-size: 3.8rem !important;
}

.stMarkdown h3 {

    font-size: 2.5rem !important;
}

/* ======================================================
INPUT BOXES
====================================================== */

.stTextInput > div > div > input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 14px !important;
    padding: 12px !important;
    font-size: 24px !important;
    min-height: 58px !important;
}

.stTextArea textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}


/* focus improvement */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid #7C3AED !important;
    box-shadow: 0 0 0 2px rgba(124,58,237,0.2);
}


/* ======================================================
SELECTBOX
====================================================== */

div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: white !important;
    min-height: 58px !important;
    font-size: 24px !important;
    padding-left: 8px !important;
}


/* ======================================================
BUTTONS
====================================================== */

.stButton > button {
    background: linear-gradient(135deg,#4F46E5,#7C3AED) !important;
    color: white !important;
    border: none !important;
    border-radius:16px !important;
    padding: 0.55rem 0.9rem !important;
    font-weight:700 !important;
    font-size:24px !important;
    min-height:64px !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    transition: all 0.25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 10px 25px rgba(124,58,237,0.4);
}

.stButton > button:active {
    transform: scale(0.97);
}


/* ======================================================
DOWNLOAD BUTTON
====================================================== */

.stDownloadButton button {
    background: rgba(15,23,42,0.95) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 14px !important;
    padding: 0.45rem 1rem !important;
    transition: all 0.25s ease !important;
}

.stDownloadButton button:hover {
    border: 1px solid rgba(56,189,248,0.4) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(56,189,248,0.12);
}


/* ======================================================
METRICS
====================================================== */

div[data-testid="metric-container"] {
    background: linear-gradient(135deg,rgba(15,23,42,0.95),rgba(30,41,59,0.95));
    border: 1px solid rgba(255,255,255,0.06);
    padding: 1.8rem;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
}

div[data-testid="metric-container"] label {
    color: #94A3B8 !important;
    font-size: 1.5rem !important;
    font-weight: 600 !important;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #4ADE80 !important;
    font-size: 3rem !important;
    font-weight: 800 !important;
}


/* ======================================================
DATAFRAME
====================================================== */

[data-testid="stDataFrame"] * {
    font-size: 16px !important;
    background-color: rgba(15,23,42,0.9);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.06);
}


/* ======================================================
TABS
====================================================== */

.stTabs [role="tab"] {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 14px 14px 0px 0px;
    padding: 16px 26px;
    margin-right: 8px;
    transition: 0.3s;
    font-size: 20px !important;
    font-weight: 700 !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,#4F46E5,#7C3AED) !important;
}


/* ======================================================
ALERTS
====================================================== */

.stAlert {
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.05);
}


/* ======================================================
PLOTLY
====================================================== */

.js-plotly-plot,
.plot-container {
    background: transparent !important;
}


/* ======================================================
SCROLLBAR
====================================================== */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #0F172A;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg,#4F46E5,#7C3AED);
    border-radius: 20px;
}


/* ======================================================
LINKS
====================================================== */

a {
    color: #A78BFA !important;
    text-decoration: none !important;
}

a:hover {
    color: #C4B5FD !important;
}


/* ======================================================
IMAGES
====================================================== */

img {
    border-radius: 18px;
}


/* ======================================================
EXPANDER
====================================================== */

.streamlit-expanderHeader {
    background-color: #111827 !important;
    border-radius: 12px !important;
}


/* ======================================================
CARDS
====================================================== */

.custom-card,
.explore-card,
.premium-card {
    backdrop-filter: blur(10px);
}

.custom-card {
    padding: 25px;
    border-radius: 24px;
    background: rgba(15,23,42,0.92);
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    transition: all 0.25s ease;
}

.custom-card:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(56,189,248,0.5);
}

.premium-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(168,85,247,0.5);
}


/* ======================================================
EXPLORE GRID
====================================================== */

.explore-title {

    font-size: 24px;

    font-weight: 700;

    color: #E2E8F0;

    margin-top: 14px;
}

.explore-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
}

.explore-card {
    background: rgba(15,23,42,0.92);
    border: 1px solid #1E293B;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    transition: 0.25s;
}

.explore-card:hover {
    transform: translateY(-6px);
    border: 1px solid #38BDF8;
    box-shadow: 0 12px 28px rgba(56,189,248,0.15);
}


/* ======================================================
HORIZONTAL LINE
====================================================== */

hr {
    border: 1px solid rgba(255,255,255,0.06);
}


/* ======================================================
CAPTION
====================================================== */

.caption {
    color: #94A3B8 !important;
}


/* ======================================================
RESPONSIVE
====================================================== */

@media screen and (max-width: 768px) {

    h1 { font-size: 3.8rem !important; }
    h2 { font-size: 3.4rem !important; }

    p, li, label, span {
        font-size: 1.25rem !important;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .custom-card { padding: 18px !important; }
    .explore-card { padding: 16px !important; }

    .stButton > button {
        font-size: 42px !important;
    }
}

/* ======================================================
MENU BUTTON FIX
====================================================== */

div[data-testid="column"]:first-child .stButton {

    display: flex !important;

    justify-content: center !important;

    align-items: center !important;
}

div[data-testid="column"]:first-child .stButton button {

    width: 95px !important;

    min-width: 95px !important;

    height: 64px !important;

    border-radius: 18px !important;

    font-size: 34px !important;

    font-weight: 700 !important;

    padding: 0 !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    overflow: visible !important;
}

.element-container {
    
    margin-bottom: 0.3rem !important;
}

/* ======================================================
MENU GRID LAYOUT
====================================================== */

.menu-wrapper {

    background: rgba(15,23,42,0.92);

    padding: 30px;

    border-radius: 24px;

    border: 1px solid rgba(255,255,255,0.06);

    margin-bottom: 30px;

    backdrop-filter: blur(12px);
}

/* Menu Header */

.menu-title {

    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 8px;
}

.menu-title span {

    font-size: 42px;

    colour: white;
}

.menu-title h2 {

    margin: 0;

    font-size: 42px !important;

    font-weight: 800 !important;
}

/* Menu Subtitle */

.menu-subtitle {

    font-size: 22px;

    color: #CBD5E1;

    margin-top: 10px;

    margin-bottom: 35px;
    
    line-height: 1.7;
}

/* Grid Layout */

.menu-grid {

    display: grid;

    grid-template-columns: repeat(2, minmax(220px, 1fr));

    gap: 18px;

}

/* ======================================================
INFO / SUCCESS / WARNING BOX SIZE
====================================================== */

.stAlert {

    padding: 22px !important;

    border-radius: 20px !important;

    font-size: 18px !important;

    line-height: 1.8 !important;
}

/* Info Text */

.stAlert p {

    font-size: 18px !important;

    font-weight: 500 !important;
}

</style>
""",
        unsafe_allow_html=True
    )