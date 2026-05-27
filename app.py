# =========================================================
# CLARITY INVEST PRO - MAIN APP
# =========================================================

import streamlit as st

from styles import load_css
from home import show_home_page
from analysis import show_analysis_page
from comparison import show_comparison_page
from sip import show_sip_page
from portfolio import show_portfolio_page
from premium import show_premium_page
from contact import show_contact_page

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Clarity Invest Pro",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD CSS
# =========================================================

load_css()

# =========================================================
# SESSION STATE INIT
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
# HEADER
# =========================================================

col1, col2 = st.columns([1.2, 8.8], gap="small")

with col1:

    menu_icon = "✕ CLOSE" if st.session_state.menu else "☰ MENU"

    if st.button(menu_icon, key="menu_toggle"):
        st.session_state.menu = not st.session_state.menu
        st.rerun()

with col2:

    st.markdown("""
    <h1 style="
    <div style="
    display:flex;
    align-items:center;
    height:100%;
    ">
    font-size:52px;
    font-weight:800;
    margin-top:0;
    margin-bottom:0;
    color:white;
    letter-spacing:-1px;
    ">
    ⚡ Clarity Invest Pro
    </h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# SLIDE MENU
# =========================================================

if st.session_state.menu:

    st.markdown("""
    <div style="
    padding:1px 0;
">

<h3 style="
    color: white;
    margin-bottom:6px;
    font-size:35px;
    font-weight: 600;
    letter-spacing: 0.3px;
">
☰ Quick Menu
</h3>

<p style="
    color: #94A3B8;
    margin: 0;
    font-size:35px;
    display: flex;
    align-items: center;
    gap:6px;
">
Try more tools <span style="color:#38BDF8;">→</span>
</p>

</div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns([1,1], gap="small")

    with colA:
        if st.button("📈 Analysis", key="menu_analysis"):
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

    st.markdown("---")

    if st.button("❌ Close Menu"):
        st.session_state.menu = False
        st.rerun()

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

st.markdown("""
<div style='text-align:center; color:#94A3B8; font-size:26px; line-height:1.6;'>
<b>⚡ Clarity Invest Pro</b><br>
Smart investing made simple<br>
Educational Purpose Only
</div>
""", unsafe_allow_html=True)