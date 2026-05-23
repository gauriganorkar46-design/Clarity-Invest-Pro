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

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # =====================================================
    # LOGO / BRANDING
    # =====================================================

    st.markdown(
        """
<div style='text-align:center;padding-top:20px;'>

<h1 style='
font-size:42px;
font-weight:800;
margin-bottom:0px;
'>
⚡Clarity Invest
</h1>

<p style='
color:#9CA3AF;
font-size:18px;
margin-top:5px;
'>
Simplifying Investing
</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # NAVIGATION
    # =====================================================

    st.subheader("📌 Navigation")

    # =====================================================
    # HOME
    # =====================================================

    if st.button(

        "🏠 Home",

        use_container_width=True

    ):

        st.session_state.page = "home"

    # =====================================================
    # ANALYSIS
    # =====================================================

    if st.button(

        "📈 Stock Analysis",

        use_container_width=True

    ):

        st.session_state.page = "analysis"

    # =====================================================
    # COMPARISON
    # =====================================================

    if st.button(

        "⚖️ Compare Stocks",

        use_container_width=True

    ):

        st.session_state.page = "compare"

    # =====================================================
    # SIP
    # =====================================================

    if st.button(

        "💰 SIP Calculator",

        use_container_width=True

    ):

        st.session_state.page = "sip"

    # =====================================================
    # PORTFOLIO
    # =====================================================

    if st.button(

        "📘 Portfolio Tool",

        use_container_width=True

    ):

        st.session_state.page = "portfolio"

    # =====================================================
    # PREMIUM
    # =====================================================

    if st.button(

        "💎 Premium Guidance",

        use_container_width=True

    ):

        st.session_state.page = "premium"

    # =====================================================
    # CONTACT
    # =====================================================

    if st.button(

        "📩 Contact",

        use_container_width=True

    ):

        st.session_state.page = "contact"

    st.markdown("---")

    # =====================================================
    # QUICK INFO
    # =====================================================

    st.info(
        """
Beginner-friendly investing dashboard designed to simplify finance concepts.
"""
    )

    st.caption(
        """
Educational purpose only.
No financial advice.
"""
    )

# =========================================================
# PAGE ROUTING
# =========================================================

# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    show_home_page()

# =========================================================
# ANALYSIS PAGE
# =========================================================

elif st.session_state.page == "analysis":

    show_analysis_page()

# =========================================================
# COMPARISON PAGE
# =========================================================

elif st.session_state.page == "compare":

    show_comparison_page()

# =========================================================
# SIP PAGE
# =========================================================

elif st.session_state.page == "sip":

    show_sip_page()

# =========================================================
# PORTFOLIO PAGE
# =========================================================

elif st.session_state.page == "portfolio":

    show_portfolio_page()

# =========================================================
# PREMIUM PAGE
# =========================================================

elif st.session_state.page == "premium":

    show_premium_page()

# =========================================================
# CONTACT PAGE
# =========================================================

elif st.session_state.page == "contact":

    show_contact_page()

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
<div style='
text-align:center;
padding:20px;
color:#94A3B8;
font-size:25px;
'>

<p>
⚡Clarity Invest Pro Dashboard
</p>

<p>
Built for beginner-friendly investing understanding
</p>

<p>
Educational Purpose Only • No Guaranteed Returns
</p>

</div>
""",
    unsafe_allow_html=True
)