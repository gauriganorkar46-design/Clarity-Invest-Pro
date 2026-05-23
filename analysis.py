# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import yfinance as yf
import pandas as pd

from yahooquery import search

from charts import show_chart_section
from news import show_news_section

# =========================================================
# SECTOR INSIGHT FUNCTION
# =========================================================

def get_sector_insight(sector, trend):

    insights = {

        "Technology": {

        "Positive Trend":
            "Technology sector is benefiting from digital transformation and innovation demand.",

        "Neutral Trend":
            "Technology sector is currently facing weaker momentum and market volatility."
        },

        "Financial Services": {

            "Positive Trend":
                "Financial companies are benefiting from stronger market confidence and lending activity.",

            "Neutral Trend":
                "Financial sector is currently impacted by economic uncertainty and interest rate pressure."
        },

        "Energy": {

            "Positive Trend":
                "Energy companies are benefiting from stronger fuel demand and pricing conditions.",

            "Neutral Trend":
                "Energy companies are facing pressure from oil price fluctuations."
        },

        "Healthcare": {

            "Positive Trend":
                "Healthcare sector remains supported by stable medical demand.",

            "Neutral Trend":
                "Healthcare companies remain relatively defensive despite weaker momentum."
        },

        "Industrials": {

            "Positive Trend":
                "Industrial companies are benefiting from infrastructure and manufacturing activity.",

            "Neutral Trend":
                "Industrial sector is facing slower economic activity."
        },

        "Consumer Defensive": {

            "Positive Trend":
                "Consumer defensive companies are showing stable long-term demand.",

            "Neutral Trend":
                "Consumer defensive sector remains comparatively resilient."
        },

        "Consumer Cyclical": {

            "Positive Trend":
                "Consumer-focused companies are benefiting from stronger consumer demand.",

            "Neutral Trend":
                "Changing consumer spending patterns are affecting cyclical demand."
        },

        "Transportation": {

            "Positive Trend":
                "Transportation companies are benefiting from stronger logistics demand.",

            "Neutral Trend":
                "Transportation sector is facing operational and fuel-cost pressures."
        },

        "Communication Services": {

            "Positive Trend":
                "Communication companies are benefiting from rising digital connectivity demand.",

            "Neutral Trend":
                "Communication sector is facing stronger competition and slower momentum."
        },
        
        "Basic Materials": {

            "Positive Trend":
                "Basic materials companies are benefiting from industrial and construction demand.",

            "Neutral Trend":
                "Commodity price fluctuations are affecting the materials sector."
        },

        "Real Estate": {

            "Positive Trend":
                "Real estate companies are benefiting from stronger property and infrastructure activity.",

            "Neutral Trend":
                "Real estate sector is facing pressure from interest rates and slower demand."
        },

        "Utilities": {

            "Positive Trend":
                "Utilities sector is benefiting from stable energy and infrastructure demand.",

            "Neutral Trend":
                "Utilities remain comparatively stable despite slower growth."
        },

        "Consumer Staples": {

            "Positive Trend":
                "Consumer staples companies are supported by stable daily consumption demand.",

            "Neutral Trend":
                "Consumer staples sector remains relatively defensive in weaker markets."
        },

        "Communication": {

            "Positive Trend":
                "Communication companies are benefiting from growing media and connectivity demand.",

            "Neutral Trend":
                "Communication sector is facing competitive and advertising pressures."
        },

        "Real Estate Services": {

            "Positive Trend":
                "Real estate services are benefiting from improving property market activity.",

            "Neutral Trend":
                "Property-related businesses are currently facing slower market movement."
        },

        "Airlines": {

            "Positive Trend":
                "Airline companies are benefiting from stronger travel demand and tourism activity.",

            "Neutral Trend":
                "Airline companies are affected by fuel price volatility and changing travel demand."
        },

        "Railroads": {

            "Positive Trend":
                "Railway companies are benefiting from transportation and infrastructure growth.",

            "Neutral Trend":
                "Railway companies are currently facing slower industrial movement."
        },

        "Auto Manufacturers": {

            "Positive Trend":
                "Automobile companies are benefiting from rising consumer and EV demand.",

            "Neutral Trend":
                "Auto companies are facing supply-chain and demand-related pressures."
        },

        "Banks": {

            "Positive Trend":
                "Banks are benefiting from lending growth and economic activity.",

            "Neutral Trend":
                "Banking sector is currently facing economic and interest rate pressures."
        }

    }

    if sector in insights:

        return insights[sector].get(

            trend,

            "Sector is reacting to broader market conditions."

        )

    return "This sector reacts to overall market and economic conditions."

# =========================================================
# OBSERVATION FUNCTION
# =========================================================

def get_observation(risk, trend):

    if trend == "Positive Trend" and risk == "Low Risk":

        return (
            "Stable stock showing positive momentum with comparatively lower volatility."
        )

    elif trend == "Positive Trend" and risk == "Moderate Risk":

        return (
            "Stock is showing healthy growth with manageable fluctuations."
        )

    elif trend == "Positive Trend" and risk == "High Risk":

        return (
            "Strong growth potential exists, but volatility is comparatively higher."
        )

    elif trend == "Neutral Trend" and risk == "Low Risk":

        return (
            "Stock remains stable, but momentum is currently limited."
        )

    elif trend == "Neutral Trend" and risk == "Moderate Risk":

        return (
            "Moderate volatility with weaker momentum currently."
        )

    elif trend == "Neutral Trend" and risk == "High Risk":

        return (
            "Higher volatility and weaker movement indicate cautious investing."
        )

    return "Insufficient information available for detailed observation."

# =========================================================
# VALID TICKER
# =========================================================

def get_valid_ticker(company):

    try:

        result = search(company)

        if (

            'quotes' not in result

            or len(result['quotes']) == 0

        ):

            return None

        for item in result['quotes']:

            symbol = item.get('symbol')

            quote_type = item.get('quoteType')

            if (

                symbol

                and quote_type == "EQUITY"

            ):

                return symbol

        return result['quotes'][0].get('symbol')

    except Exception:

        return None

# =========================================================
# MAIN ANALYSIS FUNCTION
# =========================================================

@st.cache_data(ttl=3600)

def analyze_stock(company, period):

    try:

        # =================================================
        # GET TICKER
        # =================================================

        stock = get_valid_ticker(company)

        if not stock:

            return None

        # =================================================
        # PERIOD LOGIC
        # =================================================

        period_map = {

            "Short Term": "6mo",

            "Medium Term": "1y",

            "Long Term": "5y"

        }

        yf_period = period_map.get(period, "1y")

        # =================================================
        # DOWNLOAD DATA
        # =================================================

        data = yf.download(

            stock,

            period=yf_period,

            progress=False,

            auto_adjust=False

        )

        if data.empty:

            return None

        # =================================================
        # MULTIINDEX FIX
        # =================================================

        if isinstance(data.columns, pd.MultiIndex):

            data.columns = data.columns.get_level_values(0)

        # =================================================
        # REQUIRED COLUMNS
        # =================================================

        required_cols = [

            'Open',
            'High',
            'Low',
            'Close',
            'Volume'

        ]

        if not all(col in data.columns for col in required_cols):

            return None

        # =================================================
        # CLEAN DATA
        # =================================================

        data = data.dropna()

        if len(data) < 20:

            return None

        close_prices = data['Close'].squeeze()

        # =================================================
        # RETURNS & VOLATILITY
        # =================================================

        data['Returns'] = close_prices.pct_change()

        volatility = float(

            data['Returns'].std()

        )

        # =================================================
        # MOVING AVERAGES
        # =================================================

        data['MA20'] = (

            close_prices

            .rolling(window=20)

            .mean()

        )

        data['MA50'] = (

            close_prices

            .rolling(window=50)

            .mean()

        )

        data['MA200'] = (

            close_prices

            .rolling(window=200)

            .mean()

        )

        # =================================================
        # PRICE INFORMATION
        # =================================================

        current_price = float(

            close_prices.iloc[-1]

        )

        start_price = float(

            close_prices.iloc[0]

        )

        change_percent = (

            (

                (current_price - start_price)

                / start_price

            ) * 100

        )

        # =================================================
        # RISK LOGIC
        # =================================================

        if volatility < 0.02:

            risk = "Low Risk"

        elif volatility < 0.05:

            risk = "Moderate Risk"

        else:

            risk = "High Risk"

        # =================================================
        # TREND LOGIC
        # =================================================

        ma20 = data['MA20'].iloc[-1]
        ma50 = data['MA50'].iloc[-1]
        ma200 = data['MA200'].iloc[-1]

        if period == "Short Term":

            if pd.isna(ma20):

                trend = "Insufficient Data"

            elif current_price > ma20:

                trend = "Positive Trend"

            else:

                trend = "Neutral Trend"

        elif period == "Medium Term":

            if pd.isna(ma20) or pd.isna(ma50):

                trend = "Insufficient Data"

            elif ma20 > ma50:

                trend = "Positive Trend"

            else:

                trend = "Neutral Trend"

        else:

            if pd.isna(ma50) or pd.isna(ma200):

                trend = "Insufficient Data"

            elif ma50 > ma200:

                trend = "Positive Trend"

            else:

                trend = "Neutral Trend"

        # =================================================
        # COMPANY INFO
        # =================================================

        try:

            ticker = yf.Ticker(stock)

            info = ticker.info

            sector = info.get(

                "sector",

                "Other"

            )

        except Exception:

            sector = "Other"

        # =================================================
        # INSIGHTS
        # =================================================

        observation = get_observation(

            risk,
            trend

        )

        sector_insight = get_sector_insight(

            sector,
            trend

        )

        # =================================================
        # RETURN RESULTS
        # =================================================

        return {

            "Company": company.title(),

            "Ticker": stock,

            "Sector": sector,

            "Current Price": round(current_price, 2),

            "Price Change": round(change_percent, 2),

            "Risk": risk,

            "Trend": trend,

            "Volatility": round(volatility, 4),

            "Observation": observation,

            "Sector Insight": sector_insight,

            "Data": data

        }

    except Exception:

        return None

# =========================================================
# ANALYSIS PAGE
# =========================================================

def show_analysis_page():

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
font-size:72px;
font-weight:800;
margin-bottom:10px;
'>
📊 Stock Analysis Dashboard
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Beginner-friendly stock understanding platform
</h3>

<p style='
color:#CBD5E1;
font-size:25px;
line-height:1.8;
'>
Analyze company trends, risk, volatility, charts, and market behavior in a simplified way.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.info(
        """
This dashboard helps beginners understand:
        
✅ stock movement  
✅ trend behavior  
✅ volatility  
✅ market momentum  
✅ risk understanding  
"""
    )

    st.markdown("---")

    # =====================================================
    # INPUTS
    # =====================================================

    input_col1, input_col2 = st.columns(2)

    with input_col1:

        company = st.text_input(

            "Enter Company Name",

            "Reliance"

        )

    with input_col2:

        period = st.selectbox(

            "Select Investment Period",

            [

                "Short Term",
                "Medium Term",
                "Long Term"

            ]

        )

    analyze_button = st.button(
        "🚀 Analyze Stock",
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # ANALYSIS
    # =====================================================

    if analyze_button:

        with st.spinner("Analyzing stock..."):

            result = analyze_stock(

                company,
                period

            )

        if result:

            # =================================================
            # METRICS
            # =================================================

            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

            metric_col1.metric(

                "Current Price",

                f"₹{result['Current Price']}"

            )

            metric_col2.metric(

                "Price Change %",

                f"{result['Price Change']}%"

            )

            metric_col3.metric(

                "Risk Level",

                result['Risk']

            )

            metric_col4.metric(

                "Trend",

                result['Trend']

            )

            st.markdown("---")

            # =================================================
            # TABS
            # =================================================

            tab1, tab2, tab3, tab4 = st.tabs([

                "📈 Interactive Charts",

                "💡 Insights",

                "🔎 Historical Data",

                "📰 Latest News"

            ])

            # =================================================
            # TAB 1 — CHARTS
            # =================================================

            with tab1:

                show_chart_section(result)

            # =================================================
            # TAB 2 — INSIGHTS
            # =================================================

            with tab2:

                st.subheader("🏢 Company Information")

                st.write(f"**Company:** {result['Company']}")
                st.write(f"**Ticker:** {result['Ticker']}")
                st.write(f"**Sector:** {result['Sector']}")
                st.write(f"**Volatility:** {result['Volatility']}")

                st.markdown("---")

                st.subheader("📊 Investment Observation")

                st.info(result['Observation'])

                st.subheader("💡 Sector Insight")

                st.success(result['Sector Insight'])

                st.subheader("⚠️ Reminder")

                st.warning(
                    "Investment decisions should align with your financial goals and risk comfort."
                )

            # =================================================
            # TAB 3 — DATA
            # =================================================

            with tab3:

                st.subheader("🔎 Historical Stock Data")

                st.dataframe(

                    result['Data'].tail(100),

                    use_container_width=True

                )

            # =================================================
            # TAB 4 — NEWS
            # =================================================

            with tab4:

                show_news_section(result['Ticker'])

            # =================================================
            # SENTIMENT
            # =================================================

            st.markdown("---")

            st.header("🤖 Investment Sentiment")

            sentiment = ""

            if (

                result['Trend'] == "Positive Trend"

                and result['Risk'] == "Low Risk"

            ):

                sentiment = "✅ BUY"

            elif (

                result['Trend'] == "Positive Trend"

                and result['Risk'] == "Moderate Risk"

            ):

                sentiment = "📍 HOLD"

            else:

                sentiment = "⚠️ SELL CAUTION"

            st.subheader(sentiment)

            st.write(
                """
This sentiment is generated using:
                
- trend analysis
- risk analysis
- moving averages
- historical volatility
"""
            )

            st.caption(
                "Educational purpose only. Not financial advice."
            )

        else:

            st.error(
                "Unable to analyze the selected company currently."
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