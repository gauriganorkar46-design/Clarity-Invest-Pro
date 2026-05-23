# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from analysis import analyze_stock

# =========================================================
# COMPARISON PAGE
# =========================================================

def show_comparison_page():

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
font-size:60px;
font-weight:800;
margin-bottom:10px;
'>
⚖️ Stock Comparison Dashboard
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Compare companies in a beginner-friendly way
</h3>

<p style='
color:#CBD5E1;
font-size:18px;
line-height:1.8;
'>
Understand differences in company performance, risk, sector behavior, and market trends.
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
This comparison tool helps beginners understand:
        
✅ Performance differences  
✅ Risk comparison  
✅ Sector behavior  
✅ Market trends  
✅ Relative company movement  
"""
    )

    st.markdown("---")

    # =====================================================
    # INPUT SECTION
    # =====================================================

    st.subheader("⚙️ Select Companies")

    comparison_input = st.multiselect(

        "Choose Popular Companies",

        [

            "Reliance",
            "Infosys",
            "TCS",
            "HDFC Bank",
            "ICICI Bank",
            "SBI",
            "Wipro",
            "Tata Motors",
            "Mahindra & Mahindra",
            "ITC"

        ]

    )

    custom_companies = st.text_input(

        "Or Enter Custom Companies (comma separated)",

        ""

    )

    period = st.selectbox(

        "Select Investment Period",

        [

            "Short Term",
            "Medium Term",
            "Long Term"

        ]

    )

    compare_button = st.button(
        "🚀 Compare Companies",
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # COMPARISON LOGIC
    # =====================================================

    if compare_button:

        comparison_results = []

        companies = comparison_input.copy()

        # =================================================
        # CUSTOM COMPANIES
        # =================================================

        if custom_companies:

            custom_list = custom_companies.split(",")

            for comp in custom_list:

                comp = comp.strip()

                if comp and comp not in companies:

                    companies.append(comp)

        # =================================================
        # LIMIT CHECK
        # =================================================

        if len(companies) > 8:

            st.warning(
                "Please compare maximum 8 companies at once."
            )

            st.stop()

        # =================================================
        # EMPTY CHECK
        # =================================================

        if len(companies) == 0:

            st.warning(
                "Please select or enter companies."
            )

            st.stop()

        # =================================================
        # ANALYZE COMPANIES
        # =================================================

        with st.spinner("Comparing companies..."):

            for comp in companies:

                result = analyze_stock(
                    comp,
                    period
                )

                if result:

                    comparison_results.append(result)

        # =================================================
        # RESULTS
        # =================================================

        if len(comparison_results) > 0:

            st.subheader("📑 Comparison Summary")

            comparison_df = pd.DataFrame([

                {

                    "Company": r["Company"],
                    "Sector": r["Sector"],
                    "Current Price": r["Current Price"],
                    "Price Change %": r["Price Change"],
                    "Risk": r["Risk"],
                    "Trend": r["Trend"]

                }

                for r in comparison_results

            ])

            st.dataframe(
                comparison_df,
                use_container_width=True
            )

            st.markdown("---")

            # =============================================
            # NORMALIZED PERFORMANCE CHART
            # =============================================

            st.subheader("📊 Performance Comparison")

            comparison_fig = go.Figure()

            for r in comparison_results:

                normalized = (

                    r['Data']['Close']

                    /

                    r['Data']['Close'].iloc[0]

                )

                comparison_fig.add_trace(

                    go.Scatter(

                        x=r['Data'].index,

                        y=normalized,

                        mode='lines',

                        name=r['Company']

                    )

                )

            comparison_fig.update_layout(

                template="plotly_dark",

                height=650,

                title="Normalized Company Performance",

                xaxis_title="Date",

                yaxis_title="Normalized Performance"

            )

            st.plotly_chart(
                comparison_fig,
                use_container_width=True
            )

            st.markdown("---")

            # =============================================
            # BEGINNER INSIGHTS
            # =============================================

            st.subheader("💡 Beginner Comparison Understanding")

            st.write(
                """
Comparing companies helps beginners understand:

- differences in market movement
- risk variation
- sector behavior
- relative performance
- volatility differences

Normalized charts help compare companies fairly even if stock prices are very different.
"""
            )

            # =============================================
            # OBSERVATION SECTION
            # =============================================

            st.markdown("---")

            st.subheader("🧠 Important Beginner Reminder")

            st.warning(
                """
Different companies may behave differently depending on:
                
- market conditions
- sector performance
- company fundamentals
- economic conditions
- investor sentiment

Comparison should be used for understanding and learning purposes.
"""
            )

        else:

            st.error(
                "No valid companies found for comparison."
            )

    # =====================================================
    # PREMIUM CTA
    # =====================================================

    st.markdown("---")

    st.subheader("👑 Want Personalized Investing Guidance?")

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

<p style='color:#E5E7EB;font-size:25px;'>

Understand:
        
✅ stock comparison  
✅ risk comfort  
✅ investing understanding  
✅ beginner portfolio thinking  
✅ long-term investing clarity  

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