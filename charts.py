# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import plotly.graph_objects as go

from plotly.subplots import make_subplots

# =========================================================
# CHART SECTION
# =========================================================

def show_chart_section(result):

    # =====================================================
    # DATA
    # =====================================================

    data = result['Data']

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        f"""
<div style='
padding:30px;
border-radius:24px;
background: linear-gradient(135deg,#0F172A,#1E293B,#312E81);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:25px;
'>

<h1 style='
color:white;
font-size:42px;
font-weight:800;
margin-bottom:10px;
'>
📈 Interactive Stock Chart
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:15px;
'>
{result['Company']} ({result['Ticker']})
</h3>

<p style='
color:#CBD5E1;
font-size:17px;
line-height:1.8;
'>
Analyze stock movement, trends, momentum, and trading activity using interactive visualization.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    # =====================================================
    # BEGINNER INFO
    # =====================================================

    st.info(
        """
This chart helps beginners understand:
        
✅ price movement  
✅ market trend  
✅ trading activity  
✅ momentum behavior  
✅ volatility patterns  
"""
    )

    st.markdown("---")

    # =====================================================
    # CREATE SUBPLOTS
    # =====================================================

    fig = make_subplots(

        rows=2,
        cols=1,

        shared_xaxes=True,

        vertical_spacing=0.04,

        row_heights=[0.75, 0.25]

    )

    # =====================================================
    # CANDLESTICK
    # =====================================================

    fig.add_trace(

        go.Candlestick(

            x=data.index,

            open=data['Open'],

            high=data['High'],

            low=data['Low'],

            close=data['Close'],

            name='Price'

        ),

        row=1,
        col=1

    )

    # =====================================================
    # MOVING AVERAGES
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data['MA20'],

            mode='lines',

            name='MA20'

        ),

        row=1,
        col=1

    )

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data['MA50'],

            mode='lines',

            name='MA50'

        ),

        row=1,
        col=1

    )

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data['MA200'],

            mode='lines',

            name='MA200'

        ),

        row=1,
        col=1

    )

    # =====================================================
    # VOLUME CHART
    # =====================================================

    fig.add_trace(

        go.Bar(

            x=data.index,

            y=data['Volume'],

            name='Volume'

        ),

        row=2,
        col=1

    )

    # =====================================================
    # LAYOUT
    # =====================================================

    fig.update_layout(

        template="plotly_dark",

        height=780,

        title=f"{result['Company']} Stock Analysis",

        xaxis_rangeslider_visible=False,

        margin=dict(

            l=20,
            r=20,
            t=60,
            b=20

        )

    )

    # =====================================================
    # DISPLAY CHART
    # =====================================================

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # BEGINNER LEARNING
    # =====================================================

    st.subheader("📚 Beginner Chart Understanding")

    st.write(
        """
Candlestick charts help visualize:
        
- opening and closing price
- intraday movement
- price momentum
- volatility behavior

Moving averages help beginners identify broader trend direction instead of focusing only on short-term fluctuations.

Volume helps understand trading activity and market participation.
"""
    )

    # =====================================================
    # KEY INDICATORS
    # =====================================================

    st.markdown("---")

    st.subheader("💡 Important Indicators")

    indicator_col1, indicator_col2, indicator_col3 = st.columns(3)

    with indicator_col1:

        st.success(
            """
📈 MA20
            
Shows short-term momentum and recent market movement.
"""
        )

    with indicator_col2:

        st.info(
            """
📊 MA50
            
Helps understand medium-term trend direction.
"""
        )

    with indicator_col3:

        st.warning(
            """
📉 MA200
            
Widely used for long-term market trend analysis.
"""
        )

    # =====================================================
    # IMPORTANT REMINDER
    # =====================================================

    st.markdown("---")

    st.warning(
        """
⚠️ Reminder:
        
Charts should be used for educational understanding and market observation.
        
Short-term market movement can remain volatile and unpredictable.
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
        
✅ chart reading basics  
✅ trend understanding  
✅ risk behavior  
✅ beginner investing  
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