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

with col2:
    st.title("⚡ Clarity Invest Pro")

st.markdown("---")

# =========================================================
# SLIDE MENU (ONLY WHEN OPEN)
# =========================================================

if st.session_state.menu:

    st.markdown(
    """
    <style>
    div.stButton > button {
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
        background:#0F172A;
        padding:15px;
        border-radius:12px;
        margin-bottom:10px;
        ">
        <h3 style="color:white;">Quick Menu</h3>
        <p style="color:#94A3B8;">Navigate faster</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    colA, colB = st.columns(2)

    with colA:
        if st.button("📈 Analysis",key="menu_analysis"):
            navigate("analysis")

        if st.button("💰 SIP", key="menu_sip"):
            navigate("sip")

        if st.button("📘 Portfolio", key="menu_portfolio"):
            navigate("portfolio")

    with colB:
        if st.button("⚖️ Compare", key="menu_compare"):
            navigate("compare")

        if st.button("💎 Premium", key="menu_premium"):
            navigate("premium")

        if st.button("📩 Contact", key="menu_contact"):
            navigate("contact")

        if st.button("🏠 Home", key="menu_home"):
            navigate("home")

    if st.button("❌ Close Menu", use_container_width=False):
        st.session_state.menu = False

    st.markdown("---")


# =========================================================
# PAGE ROUTING
# =========================================================

if st.session_state.page == "home":
    show_home_page()

elif st.session_state.page == "analysis":
    show_analysis_page()

elif st.session_state.page == "compare":
    show_comparison_page()

elif st.session_state.page == "sip":
    show_sip_page()

elif st.session_state.page == "portfolio":
    show_portfolio_page()

elif st.session_state.page == "premium":
    show_premium_page()

elif st.session_state.page == "contact":
    show_contact_page()

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
