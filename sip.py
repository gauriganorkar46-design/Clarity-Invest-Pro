# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import plotly.graph_objects as go

# =========================================================
# SIP PAGE
# =========================================================

def show_sip_page():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
<div style='
padding:40px;
border-radius:28px;
background: linear-gradient(135deg,#0F172A,#1E293B,#312E81);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:25px;
'>

<h1 style='
color:white;
font-size:52px;
font-weight:800;
margin-bottom:10px;
'>
💰 SIP Calculator
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Understand long-term investing growth in a beginner-friendly way
</h3>

<p style='
color:#CBD5E1;
font-size:18px;
line-height:1.8;
'>
Estimate how regular monthly investing may grow over time using the power of compounding.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    # =====================================================
    # INTRO SECTION
    # =====================================================

    st.info(
        """
A SIP (Systematic Investment Plan) allows investing a fixed amount regularly over time.

This calculator helps beginners understand:
        
✅ Long-term investing  
✅ Compounding growth  
✅ Wealth accumulation  
✅ Investment discipline  
"""
    )

    st.markdown("---")

    # =====================================================
    # INPUT SECTION
    # =====================================================

    st.subheader("⚙️ SIP Details")

    col1, col2, col3 = st.columns(3)

    with col1:

        sip_amount = st.number_input(

            "Monthly SIP Amount (₹)",

            min_value=500,

            value=5000,

            step=500

        )

    with col2:

        years = st.slider(

            "Investment Duration (Years)",

            1,

            40,

            10

        )

    with col3:

        expected_return = st.slider(

            "Expected Annual Return (%)",

            1,

            30,

            12

        )

    st.markdown("---")

    # =====================================================
    # SIP CALCULATION
    # =====================================================

    monthly_return = expected_return / 12 / 100

    months = years * 12

    future_value = sip_amount * (

        (
            (1 + monthly_return) ** months - 1
        )

        / monthly_return

    ) * (1 + monthly_return)

    total_invested = sip_amount * months

    wealth_gained = future_value - total_invested

    # =====================================================
    # METRICS
    # =====================================================

    st.subheader("📊 Investment Projection")

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:

        st.metric(

            "Total Invested",

            f"₹{total_invested:,.0f}"

        )

    with metric_col2:

        st.metric(

            "Estimated Value",

            f"₹{future_value:,.0f}"

        )

    with metric_col3:

        st.metric(

            "Estimated Returns",

            f"₹{wealth_gained:,.0f}"

        )

    st.markdown("---")

    # =====================================================
    # VISUALIZATION
    # =====================================================

    chart_col1, chart_col2 = st.columns([1, 1])

    # =====================================================
    # PIE CHART
    # =====================================================

    with chart_col1:

        st.subheader("📈 Investment Breakdown")

        pie_fig = go.Figure(

            data=[

                go.Pie(

                    labels=[
                        "Invested Amount",
                        "Estimated Returns"
                    ],

                    values=[
                        total_invested,
                        wealth_gained
                    ],

                    hole=0.45
                )

            ]

        )

        pie_fig.update_layout(

            template="plotly_dark",

            height=420
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

    # =====================================================
    # GROWTH INFO
    # =====================================================

    with chart_col2:

        st.subheader("💡 SIP Understanding")

        st.markdown(
            """
<div style='
padding:25px;
border-radius:22px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
'>

<h3 style='color:white;'>
Why SIP Is Popular
</h3>

<p style='color:#D1D5DB;font-size:17px;line-height:1.8;'>

✅ Encourages investing discipline  

✅ Supports long-term investing  

✅ Helps understand compounding  

✅ Beginner-friendly investing approach  

✅ Reduces emotional investing decisions  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # LONG TERM LEARNING
    # =====================================================

    st.markdown("---")

    st.subheader("📚 Beginner Investing Understanding")

    st.write(
        """
Long-term investing focuses on consistency and patience.

Compounding allows investment growth to potentially accelerate over time because returns may also begin generating returns.

Many beginner investors use SIP investing to build long-term financial discipline gradually.
"""
    )

    # =====================================================
    # IMPORTANT REMINDER
    # =====================================================

    st.markdown("---")

    st.warning(
        """
⚠️ Reminder:
        
This SIP calculator is designed for educational and informational purposes only.
        
Actual market returns may vary depending on:
        
- market conditions
- volatility
- investment type
- time horizon
"""
    )

    # =====================================================
    # PREMIUM CTA
    # =====================================================

    st.markdown("---")

    st.subheader("🎯 Want Personalized Beginner Guidance?")

    st.markdown(
        """
<div style='
padding:25px;
border-radius:20px;
background: linear-gradient(135deg,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.06);
'>

<h3 style='color:white;'>
Get Beginner-Focused Investing Clarity
</h3>

<p style='color:#E5E7EB;font-size:17px;'>

Understand:
        
✅ SIP planning  
✅ Investing discipline  
✅ Risk comfort  
✅ Beginner investing strategy  
✅ Long-term financial understanding  

</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.info(
        "You can explore personalized beginner guidance from the Premium section."
    )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")

    st.caption(
        """
Educational purpose only.
No guaranteed returns or financial advice.
"""
    )