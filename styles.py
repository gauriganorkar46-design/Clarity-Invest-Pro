# =========================================================
# GLOBAL STYLES
# =========================================================

import streamlit as st

# =========================================================
# LOAD CSS
# =========================================================

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
GLOBAL APP BACKGROUND
====================================================== */

.stApp {
    background: linear-gradient(135deg,#020617,#071127,#0F172A);
    color: white;
}

/* ======================================================
GLOBAL TEXT FIX (MOBILE SAFE)
====================================================== */

p, li, label, span {
    color: #D1D5DB !important;
    font-size: 1rem;
    line-height: 1.6;
} 

/* ======================================================
MAIN APP
====================================================== */

.stApp {

    background:
    linear-gradient(
        135deg,
        #020617,
        #071127,
        #0F172A
    );

    color: white;
}

/* ======================================================
REMOVE DEFAULT SPACING
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

    background:
    linear-gradient(
        180deg,
        #020617,
        #0F172A
    );

    border-right:
    1px solid rgba(255,255,255,0.08);
}

/* ======================================================
SIDEBAR CONTENT
====================================================== */

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* ======================================================
HEADINGS
====================================================== */

h1 {

    color: white !important;

    font-size: 3.5rem !important;

    font-weight: 700 !important;

    letter-spacing: -1px;
}

h2 {

    color: white !important;

    font-size: 38px !important;

    font-weight: 700 !important;
}

h3 {

    color: white !important;

    font-size: 2rem !important;

    font-weight: 600 !important;
}

/* ======================================================
TEXT
====================================================== */

p,
li,
label,
span {

    color: #D1D5DB !important;

    font-size: 1.8rem;

    line-height: 1.7;
}

/* ======================================================
INPUT BOXES
====================================================== */

.stTextInput > div > div > input {

    background-color: #111827 !important;

    color: white !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    border-radius: 14px !important;

    padding: 12px !important;
}

/* ======================================================
TEXT AREA
====================================================== */

.stTextArea textarea {

    background-color: #111827 !important;

    color: white !important;

    border-radius: 14px !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;
}

/* ======================================================
SELECTBOX
====================================================== */

div[data-baseweb="select"] > div {

    background-color: #111827 !important;

    border-radius: 14px !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    color: white !important;
}

/* ======================================================
BUTTONS
====================================================== */

.stButton > button {

    background:
    linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 14px !important;

    padding: 0.55rem 1.rem !important;

    font-weight: 600 !important;

    transition: all 0.3s ease !important;

    width: 100%;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
    0px 10px 25px rgba(124,58,237,0.4);
}

.stButton > button:active {
    transform: scale(0.97);

.stDownloadButton button {

    background: rgba(15,23,42,0.95) !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    color: white !important;

    border-radius: 14px !important;

    padding: 0.55rem 1rem !important;

    transition: all 0.25s ease !important;
}

.stDownloadButton button:hover {

    border: 1px solid rgba(56,189,248,0.4) !important;

    transform: translateY(-2px);

    box-shadow: 0 8px 20px rgba(56,189,248,0.12);
}
}

/* ======================================================
METRIC CONTAINERS
====================================================== */

div[data-testid="metric-container"] {

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.95)
    );

    border:
    1px solid rgba(255,255,255,0.06);

    padding: 1.4rem;

    border-radius: 20px;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.25);
}

/* ======================================================
METRIC LABELS
====================================================== */

div[data-testid="metric-container"] label {

    color: #94A3B8 !important;

    font-size: 1.2rem !important;
}

/* ======================================================
METRIC VALUES
====================================================== */

div[data-testid="metric-container"] [data-testid="stMetricValue"] {

    color: #4ADE80 !important;

    font-size: 2.5rem !important;

    font-weight: 700 !important;
}

/* ======================================================
DATAFRAME
====================================================== */

[data-testid="stDataFrame"] {

    background-color:
    rgba(15,23,42,0.9);

    border-radius: 20px;

    overflow: hidden;

    border:
    1px solid rgba(255,255,255,0.06);
}

/* ======================================================
TABLE
====================================================== */

table {

    color: white !important;
}

/* ======================================================
TABS
====================================================== */

.stTabs [role="tab"] {

    background-color: #111827 !important;

    color: white !important;

    border-radius: 14px 14px 0px 0px;

    padding: 12px 24px;

    margin-right: 6px;

    transition: 0.3s;
}

.stTabs [aria-selected="true"] {

    background:
    linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
    ) !important;
}

/* ======================================================
INFO / ALERT BOXES
====================================================== */

.stAlert {

    border-radius: 18px !important;

    border:
    1px solid rgba(255,255,255,0.05);
}

/* ======================================================
SUCCESS BOX
====================================================== */

div[data-baseweb="notification"] {

    border-radius: 18px !important;
}

/* ======================================================
PLOTLY FIX
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

    background:
    linear-gradient(
        180deg,
        #4F46E5,
        #7C3AED
    );

    border-radius: 20px;
}

/* ======================================================
LINK BUTTONS
====================================================== */

a {

    color: #A78BFA !important;

    text-decoration: none !important;
}

a:hover {

    color: #C4B5FD !important;
}

/* ======================================================
IMAGE STYLING
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
CUSTOM CARD STYLE
====================================================== */

.custom-card {

    padding: 25px;

    border-radius: 24px;

    background:
        rgba(15,23,42,0.92),
    ;

    border:
    1px solid rgba(255,255,255,0.05);

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.25);

    transition: all 0.25s ease;
}

.custom-card:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(56,189,248,0.5);
    box-shadow: 0 8px 18px rgba(56,189,248,0.08);
}

.premium-card {
    transition: all 0.25s ease;
}

.premium-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(168,85,247,0.5);
    box-shadow: 0 8px 18px rgba(56,189,248,0.08);
}
/* ======================================================
EXPLORER CARDS
====================================================== */

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
.custom-card,
.explore-card,
.premium-card {

    backdrop-filter: blur(10px);
}

/* ======================================================
HORIZONTAL LINE
====================================================== */

hr {

    border:
    1px solid rgba(255,255,255,0.06);
}

/* ======================================================
CAPTION
====================================================== */

.caption {

    color: #94A3B8 !important;
}

/* ======================================================
MOBILE RESPONSIVE
====================================================== */

@media screen and (max-width: 768px) {

    h1 {

        font-size: 2rem !important;
    }

    h2 {

        font-size: 2rem !important;
    }
    
    p, li, label, span {
        font-size: 0.95rem !important;
    }

    .block-container {

        padding-left: 1rem;

        padding-right: 1rem;
    }

    .custom-card {

    padding: 18px !important;
    }

    .explore-card {

        padding: 16px !important;
    }

    .stButton > button {

        font-size: 14px !important;
}
}

</style>

""",
        unsafe_allow_html=True
    )