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

col1, col2 = st.columns([1.8, 10.2], gap="medium")

with col1:

    menu_icon = "✖" if st.session_state.menu else "☰"

    if st.button(menu_icon, key="menu_toggle"):
        st.session_state.menu = not st.session_state.menu
        st.rerun()

with col2:

    st.markdown(
        """
        <h1 style="
        font-size:46px;
        font-weight:800;
        color:white;
        margin-top:0;
        margin-bottom:0;
        letter-spacing:-1px;
        ">
        ⚡ Clarity Invest Pro
        </h1>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# =========================================================
# SLIDE MENU
# =========================================================

if st.session_state.menu:

    st.markdown(
        """
        <div class="menu-wrapper">

            <div class="menu-title">

                <span>☰</span>

                <h2>Quick Menu</h2>

            </div>

            <div class="menu-subtitle">
                Explore all investing tools and features
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # MENU BUTTONS
    # =====================================================

    col1, col2 = st.columns(2, gap="medium")

    with col1:
    
        st.button(
            "📈 Analysis",
            on_click=navigate,
            args=("analysis",),
            use_container_width=True
        )

        st.button(
            "💰 SIP Calculator",
            on_click=navigate,
            args=("sip",),
            use_container_width=True
        )

        st.button(
            "📘 Portfolio",
            on_click=navigate,
            args=("portfolio",),
            use_container_width=True
        )

        st.button(
            "🏠 Home",
            on_click=navigate,
            args=("home",),
            use_container_width=True
        )

    with col2:

        st.button(
            "⚖️ Compare Stocks",
            on_click=navigate,
            args=("compare",),
            use_container_width=True
        )

        st.button(
            "💎 Premium",
            on_click=navigate,
            args=("premium",),
            use_container_width=True
        )

        st.button(
            "📩 Contact",
            on_click=navigate,
            args=("contact",),
            use_container_width=True
        )

        if st.button(
            "❌ Close Menu",
            use_container_width=True
        ):
            st.session_state.menu = False
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

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