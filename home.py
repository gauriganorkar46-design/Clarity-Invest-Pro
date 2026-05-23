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
padding:50px;
border-radius:30px;
background: linear-gradient(135deg,#0F172A,#1E293B,#312E81);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:30px;
'>

<h1 style='
font-size:80px;
font-weight:800;
color:white;
margin-bottom:10px;
'>
⚡Clarity Invest Pro
</h1>

<h2 style='
font-size:50px;
font-weight:500;
color:#D1D5DB;
margin-bottom:25px;
'>
Simplifying Investing For Beginners
</h2>

<p style='
font-size:28px;
line-height:1.9;
color:#CBD5E1;
max-width:900px;
'>
Understand investing, stock trends, risk, and market behavior through a clean beginner-friendly dashboard designed to make finance easier and more practical.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    ## =====================================================
    # ENGAGEMENT SECTION (EXPLORE HOOKS)
    # =====================================================

    st.markdown("## 🚀 Your Financial Clarity Starts Here")
    st.markdown("##### Explore tools designed to simplify investing decisions")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    # =====================================================
    # COLUMN 1
    # =====================================================

    with col1:
        st.markdown(
            """
            <div style="
            background-color:#0F172A;
            padding:20px;
            border-radius:16px;
            height:160px;
            text-align:center;
            ">

            <h3 style="color:#60A5FA;">📈 “What’s Moving?”</h3>

            <p style="color:#CBD5E1; font-size:14px;">
            Find active market trends instantly
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # COLUMN 2
    # =====================================================

    with col2:
        st.markdown(
            """
            <div style="
            background-color:#0F172A;
            padding:20px;
            border-radius:16px;
            height:160px;
            text-align:center;
            ">

            <h3 style="color:#34D399;">⚖️ “Who Wins?”</h3>

            <p style="color:#CBD5E1; font-size:14px;">
            Compare companies like a pro
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # COLUMN 3
    # =====================================================

    with col3:
        st.markdown(
            """
            <div style="
            background-color:#0F172A;
            padding:20px;
            border-radius:16px;
            height:160px;
            text-align:center;
            ">

            <h3 style="color:#FBBF24;">💰 “What If You Invested?”</h3>

            <p style="color:#CBD5E1; font-size:14px;">
            Visualize your future wealth
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # COLUMN 4
    # =====================================================

    with col4:
        st.markdown(
            """
            <div style="
            background-color:#0F172A;
            padding:20px;
            border-radius:16px;
            height:160px;
            text-align:center;
            ">

            <h3 style="color:#A78BFA;">📘 “Are You Safe?”</h3>

            <p style="color:#CBD5E1; font-size:14px;">
            Check your portfolio risk in seconds
            </p>

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

<h2>
🤔 Why Clarity Invest?
</h2>

<p>
Most beginners find investing confusing because financial platforms often use complex language and technical concepts.
</p>

<p>
Clarity Invest focuses on simplifying investing through:
</p>

<ul>

<li>✅ Beginner-friendly explanations</li>

<li>✅ Risk understanding</li>

<li>✅ Real stock behavior insights</li>

<li>✅ Trend understanding</li>

<li>✅ Practical investing clarity</li>

<li>✅ Long-term learning mindset</li>

</ul>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # FEATURES
    # =====================================================

    st.header("🌟 Dashboard Features")

    feature_col1, feature_col2, feature_col3 = st.columns(3)

    # =====================================================
    # COLUMN 1
    # =====================================================

    with feature_col1:

        st.markdown(
            """
<div class='custom-card'>

<h3>📈 Stock Analysis</h3>

<p>

Analyze:
<br><br>

✅ stock trends  
✅ volatility  
✅ market movement  
✅ risk behavior  
✅ momentum analysis  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
<div class='custom-card'>

<h3>📊 Interactive Charts</h3>

<p>

Visualize:
<br><br>

✅ candlestick charts  
✅ moving averages  
✅ volume analysis  
✅ historical movement  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # COLUMN 2
    # =====================================================

    with feature_col2:

        st.markdown(
            """
<div class='custom-card'>

<h3>⚖️ Company Comparison</h3>

<p>

Compare:
<br><br>

✅ multiple companies  
✅ sector behavior  
✅ normalized performance  
✅ trend & risk  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
<div class='custom-card'>

<h3>📰 Market Information</h3>

<p>

Stay updated with:
<br><br>

✅ latest stock news  
✅ company updates  
✅ market headlines  
✅ news links  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # COLUMN 3
    # =====================================================

    with feature_col3:

        st.markdown(
            """
<div class='custom-card'>

<h3>🤖 Investment Sentiment</h3>

<p>

Generated using:
<br><br>

✅ trend analysis  
✅ moving averages  
✅ volatility  
✅ risk behavior  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
<div class='custom-card'>

<h3>💰 Financial Tools</h3>

<p>

Includes:
<br><br>

✅ SIP calculator  
✅ portfolio guidance  
✅ risk allocation  
✅ beginner support  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("---")

    # =====================================================
    # HOW IT WORKS
    # =====================================================

    st.header("⚙️ How It Works")

    work_col1, work_col2, work_col3 = st.columns(3)

    # =====================================================
    # STEP 1
    # =====================================================

    with work_col1:

        st.markdown(
            """
<div class='custom-card'>

<h2>1️⃣ Analyze</h2>

<p>

Search companies and understand:
<br><br>

✅ stock movement  
✅ volatility  
✅ risk  
✅ market trends  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # STEP 2
    # =====================================================

    with work_col2:

        st.markdown(
            """
<div class='custom-card'>

<h2>2️⃣ Compare</h2>

<p>

Compare multiple companies:
<br><br>

✅ performance  
✅ risk  
✅ trends  
✅ sector behavior  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # STEP 3
    # =====================================================

    with work_col3:

        st.markdown(
            """
<div class='custom-card'>

<h2>3️⃣ Learn</h2>

<p>

Understand investing through:
<br><br>

✅ beginner explanations  
✅ simplified finance  
✅ practical learning  
✅ investing clarity  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("---")

    # =====================================================
    # BEGINNER CTA
    # =====================================================

    st.markdown(
        """
<div style='
padding:35px;
border-radius:24px;
background: linear-gradient(135deg,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.06);
margin-top:20px;
'>

<h2 style='color:white;'>
🎯 Designed For Students & Beginners
</h2>

<p style='
color:#E5E7EB;
font-size:18px;
line-height:1.9;
'>

Clarity Invest is built to simplify investing concepts for beginners who want practical understanding instead of complicated finance terminology.

</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # TRUST NOTE
    # =====================================================

    st.caption(
        """
Educational purpose only.
No guaranteed returns or financial advice.
"""
    )