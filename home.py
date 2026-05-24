# =========================================================
# IMPORTS
# =========================================================

import streamlit as st

# =========================================================
# HOME PAGE
# =========================================================

def show_home_page():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
       
        <div style='
        padding:40px;
        border-radius:30px;
        background: linear-gradient(135deg,#0F172A,#1E293B,#312E81);
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:30px;
        '>

        <h1 style='
        font-size:60px;
        font-weight:800;
        color:white;
        margin-bottom:10px;
        '>
        ⚡Clarity Invest Pro
        </h1>

        <h2 style='
        font-size:25px;
        font-weight:500;
        color:#D1D5DB;
        margin-bottom:25px;
        '>
        Simplifying Investing For Beginners
        </h2>

        <p style='
        font-size:20px;
        line-height:1.8;
        color:#CBD5E1;
        max-width:800px;
        '>
        Understand investing, stock trends, risk, and market behavior through a clean beginner-friendly dashboard designed to make finance easier and more practical.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # EXPLORE SECTION (FINTECH STYLE CARDS)
    # =====================================================

    st.markdown("## 🚀 Your Financial Clarity Starts Here")
    st.markdown("##### Explore powerful tools designed to simplify investing decisions")

    st.markdown("---")

    st.markdown(
        """
        <style>

        .explore-title {
            font-size: 17px;
            font-weight: 600;
            color: #E2E8F0;
            margin-top: 10px;
        }

        .explore-text {
            font-size: 13px;
            color: #94A3B8;
            margin-top: 6px;
            line-height: 1.4;
        }

        .explore-badge {
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 12px;
            background: #1E293B;
            color: #38BDF8;
            display: inline-block;
        }

        </style>

        <div class="explore-grid">

        <div class="explore-card">
            <div class="explore-badge">Market Insight</div>
            <div class="explore-title">🌀 What’s Moving?</div>
            <div class="explore-text">Track real-time stock momentum and market trends instantly</div>
        </div>

        <div class="explore-card">
            <div class="explore-badge">Smart Compare</div>
            <div class="explore-title">⚖️ Who Wins?</div>
            <div class="explore-text">Compare companies side-by-side like a professional analyst</div>
        </div>

        <div class="explore-card">
            <div class="explore-badge">Future Value</div>
            <div class="explore-title">💰 What If You Invested?</div>
            <div class="explore-text">Visualize long-term wealth growth from your investments</div>
        </div>

        <div class="explore-card">
            <div class="explore-badge">Risk Check</div>
            <div class="explore-title">📘 Are You Safe?</div>
            <div class="explore-text">Analyze portfolio balance and risk exposure instantly</div>
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # WHY CLARITY INVEST
    # =====================================================

    st.markdown(
        """
        <div class='custom-card'>

        <h2>🤔 Why Clarity Invest?</h2>

        <p>
        Most beginners find investing confusing because financial platforms use complex language and technical concepts.
        </p>

        <p>We simplify investing through:</p>

        <ul>
        <li>✅ Beginner-friendly explanations</li>
        <li>✅ Risk understanding</li>
        <li>✅ Real stock behavior insights</li>
        <li>✅ Market trend clarity</li>
        <li>✅ Practical learning approach</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # FEATURES SECTION
    # =====================================================

    st.header("🌟 Dashboard Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class='custom-card'>
            <h3>💹 Stock Analysis</h3>
            <p>Understand trends, volatility, and market movement.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='custom-card'>
            <h3>📊 Charts</h3>
            <p>Interactive visual analysis of stocks.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class='custom-card'>
            <h3>⚖️ Compare Stocks</h3>
            <p>Compare companies based on performance and risk.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='custom-card'>
            <h3>📰 Market News</h3>
            <p>Latest updates and financial news.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class='custom-card'>
            <h3>🤖 Insights</h3>
            <p>AI-like sentiment and trend analysis.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='custom-card'>
            <h3>💰 Tools</h3>
            <p>SIP, portfolio and financial calculators.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # =====================================================
    # HOW IT WORKS
    # =====================================================

    st.header("⚙️ How It Works")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class='custom-card'>
            <h2>1️⃣ Analyze</h2>
            <p>Check stock behavior and trends.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class='custom-card'>
            <h2>2️⃣ Compare</h2>
            <p>Compare companies easily.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class='custom-card'>
            <h2>3️⃣ Learn</h2>
            <p>Understand investing simply.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # =====================================================
    # FINAL CTA
    # =====================================================

    st.markdown(
        """
        <div style='
        padding:30px;
        border-radius:20px;
        background: linear-gradient(135deg,#312E81,#581C87);
        color:white;
        text-align:center;
        '>

        <h2>✨ Built for Beginners</h2>
        <p>
        Simple, clear and practical investing dashboard for learning finance easily.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # FOOTNOTE
    # =====================================================

    st.caption("Educational purpose only. No financial advice.")