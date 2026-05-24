# =========================================================
# CLARITY INVEST PRO
# MAIN APPLICATION FILE
# app.py
# =========================================================

# =========================================================
# IMPORTS
# =========================================================

import streamlit as st

# =========================================================
# IMPORT SEGMENTS
# =========================================================

from styles import load_css

from home import show_home_page

from analysis import show_analysis_page

from comparison import show_comparison_page

from sip import show_sip_page

from portfolio import show_portfolio_page

from premium import show_premium_page

from contact import show_contact_page

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(

    page_title="Clarity Invest Pro",

    page_icon="🔮",

    layout="wide",

    initial_sidebar_state="expanded"

)

# =========================================================
# LOAD GLOBAL CSS
# =========================================================

load_css()

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:

    st.session_state.page = "home"

if "menu" not in st.session_state:
    st.session_state.menu = False



# =========================================================
# NAVIGATION FUNCTION
# =========================================================

def navigate(page):
    st.session_state.page = page
    st.session_state.menu = False
    st.rerun()

# =========================================================
# TOP HEADER
# =========================================================

col1, col2 = st.columns([1, 7], vertical_alignment="center")

with col1:
    st.markdown("<div style='margin-top:12px'></div>", unsafe_allow_html=True)

    if st.button("››", key="top_menu_toggle"):
        st.session_state.menu = not st.session_state.menu
        st.rerun()

with col2:
    st.title("⚡ Clarity Invest Pro")

st.markdown("---")

# =========================================================
# SIDEBAR NAVIGATION (NEW CLEAN SYSTEM)
# =========================================================

page = st.sidebar.radio(
    "📌 Navigation",
    ["🏠 Home", "📊 Analysis", "⚖️ Compare", "💰 SIP", "📘 Portfolio", "💎 Premium", "📩 Contact"]
)

# =========================================================
# PAGE ROUTING
# =========================================================

if page == "🏠 Home":
    st.session_state.page = "home"

elif page == "📊 Analysis":
    st.session_state.page = "analysis"

elif page == "⚖️ Compare":
    st.session_state.page = "compare"

elif page == "💰 SIP":
    st.session_state.page = "sip"

elif page == "📘 Portfolio":
    st.session_state.page = "portfolio"

elif page == "💎 Premium":
    st.session_state.page = "premium"

elif page == "📩 Contact":
    st.session_state.page = "contact"
    
# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center; padding:15px; color:#94A3B8; font-size:12px;'>
<b>⚡ Clarity Invest Pro</b><br>
Smart investing made simple<br>
<span style="font-size:11px;">Educational Purpose Only</span>
</div>
""",
unsafe_allow_html=True
)
