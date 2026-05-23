# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import plotly.graph_objects as go

# =========================================================
# PORTFOLIO PAGE
# =========================================================

def show_portfolio_page():

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
📘 Beginner Portfolio Guidance
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Understand portfolio allocation in a beginner-friendly way
</h3>

<p style='
color:#CBD5E1;
font-size:28px;
line-height:1.8;
'>
Learn how different risk profiles may approach portfolio allocation and long-term investing thinking.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    # =====================================================
    # INTRODUCTION
    # =====================================================

    st.info(
        """
Portfolio allocation helps beginners understand how investments may be distributed based on:
        
✅ Risk comfort  
✅ Long-term goals  
✅ Stability preference  
✅ Growth expectations  
"""
    )

    st.markdown("---")

    # =====================================================
    # RISK PROFILE
    # =====================================================

    st.subheader("⚙️ Select Your Risk Comfort")

    risk_profile = st.selectbox(

        "Choose Risk Profile",

        [
            "Low Risk",
            "Moderate Risk",
            "High Risk"
        ]

    )

    st.markdown("---")

    # =====================================================
    # LOW RISK
    # =====================================================

    if risk_profile == "Low Risk":

        st.success(
            """
Low-risk investors generally prefer:
            
✅ Stability  
✅ Lower volatility  
✅ Consistent investing approach  
"""
        )

        col1, col2 = st.columns([1, 1])

        with col1:

            st.markdown(
                """
<div style='
padding:25px;
border-radius:22px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
'>

<h2 style='color:white;'>
📊 Suggested Allocation
</h2>

<p style='color:#D1D5DB;font-size:28px;'>

• 60% Large Cap Stocks  
• 30% Index Funds  
• 10% Gold / Cash  

</p>

</div>
""",
                unsafe_allow_html=True
            )

        with col2:

            fig = go.Figure(

                data=[

                    go.Pie(

                        labels=[
                            "Large Cap",
                            "Index Funds",
                            "Gold/Cash"
                        ],

                        values=[60, 30, 10],

                        hole=0.45
                    )

                ]

            )

            fig.update_layout(

                template="plotly_dark",

                height=420
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # =====================================================
    # MODERATE RISK
    # =====================================================

    elif risk_profile == "Moderate Risk":

        st.info(
            """
Moderate-risk investors generally balance:
            
✅ Stability  
✅ Growth potential  
✅ Moderate volatility  
"""
        )

        col1, col2 = st.columns([1, 1])

        with col1:

            st.markdown(
                """
<div style='
padding:25px;
border-radius:22px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
'>

<h2 style='color:white;'>
📊 Suggested Allocation
</h2>

<p style='color:#D1D5DB;font-size:28px;'>

• 50% Large Cap Stocks  
• 30% Mid Cap Stocks  
• 20% Index Funds  

</p>

</div>
""",
                unsafe_allow_html=True
            )

        with col2:

            fig = go.Figure(

                data=[

                    go.Pie(

                        labels=[
                            "Large Cap",
                            "Mid Cap",
                            "Index Funds"
                        ],

                        values=[50, 30, 20],

                        hole=0.45
                    )

                ]

            )

            fig.update_layout(

                template="plotly_dark",

                height=420
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # =====================================================
    # HIGH RISK
    # =====================================================

    else:

        st.warning(
            """
High-risk investors may prefer:
            
✅ Higher growth potential  
✅ Aggressive investing  
✅ Greater volatility tolerance  
"""
        )

        col1, col2 = st.columns([1, 1])

        with col1:

            st.markdown(
                """
<div style='
padding:25px;
border-radius:22px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
'>

<h2 style='color:white;'>
💸 Suggested Allocation
</h2>

<p style='color:#D1D5DB;font-size:25px;'>

• 50% Growth Stocks  
• 30% Mid/Small Cap  
• 20% High-Risk Opportunities  

</p>

</div>
""",
                unsafe_allow_html=True
            )

        with col2:

            fig = go.Figure(

                data=[

                    go.Pie(

                        labels=[
                            "Growth Stocks",
                            "Mid/Small Cap",
                            "High Risk"
                        ],

                        values=[50, 30, 20],

                        hole=0.45
                    )

                ]

            )

            fig.update_layout(

                template="plotly_dark",

                height=420
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # =====================================================
    # BEGINNER LEARNING SECTION
    # =====================================================

    st.markdown("---")

    st.subheader("📚 Beginner Portfolio Understanding")

    st.write(
        """
A portfolio is a collection of investments.

Different people may build portfolios differently depending on:
        
- financial goals
- risk comfort
- investing timeline
- stability preference

Diversification is often used to reduce dependence on a single investment.
"""
    )

    # =====================================================
    # IMPORTANT REMINDER
    # =====================================================

    st.markdown("---")

    st.warning(
        """
⚠️ Reminder:
        
This portfolio tool is designed for educational and beginner-learning purposes only.
        
It does NOT provide:
        
❌ guaranteed returns  
❌ stock recommendations  
❌ financial advice  
"""
    )

    # =====================================================
    # PREMIUM CTA
    # =====================================================

    st.markdown("---")

    st.subheader("👑 Want Personalized Portfolio Guidance?")

    st.markdown(
        """
<div style='
padding:25px;
border-radius:20px;
background: linear-gradient(135deg,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.06);
'>

<h3 style='color:white;'>
Get Beginner-Focused Personalized Clarity
</h3>

<p style='color:#E5E7EB;font-size:28px;'>

Understand investing and portfolio thinking in a simplified beginner-friendly way based on:
        
✅ Your goals  
✅ Your comfort level  
✅ Beginner investing stage  
✅ Long-term understanding  

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