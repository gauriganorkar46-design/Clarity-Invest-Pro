import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from yahooquery import search

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Clarity Invest Pro",
    page_icon="📈",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""

<style>

/* ======================================================
MAIN APP
====================================================== */

.stApp {

    background: linear-gradient(
        135deg,
        #050816,
        #071127,
        #0A1931
    );

    color: white;
}

/* ======================================================
REMOVE DEFAULT STREAMLIT SPACE
====================================================== */

.block-container {

    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* ======================================================
SIDEBAR
====================================================== */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0B1220,
        #111827
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ======================================================
SIDEBAR TEXT
====================================================== */

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* ======================================================
TITLE
====================================================== */

h1 {

    color: white !important;

    font-size: 3rem !important;

    font-weight: 800 !important;

    letter-spacing: -1px;
}

/* ======================================================
HEADINGS
====================================================== */

h2, h3 {

    color: white !important;

    font-weight: 700 !important;
}

/* ======================================================
PARAGRAPH TEXT
====================================================== */

p, li, label, span {

    color: #D1D5DB !important;

    font-size: 1rem;
}

/* ======================================================
INPUT BOXES
====================================================== */

/* Text Input */
.stTextInput > div > div > input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #374151 !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

/* Placeholder text */
.stTextArea textarea::placeholder {
    color: #9CA3AF !important;
}

/* Text Area */
.stTextArea textarea {
    background-color: #111827 !important;
    color: #FFFFFF !important;
    caret-color: #FFFFFF !important;
    border: 1px solid #374151 !important;
    border-radius: 10px !important;
}

/* Selectbox container */
div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #374151 !important;
    border-radius: 10px !important;
}

/* Selectbox text */
div[data-baseweb="select"] span {
    color: white !important;
}

/* DROPDOWN OPTIONS */
ul {
    background-color: #111827 !important;
}

li {
    background-color: #111827 !important;
    color: white !important;
}

/* ======================================================
BUTTONS
====================================================== */

.stButton > button {

    background: linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 0.7rem 1.2rem !important;

    font-weight: 600 !important;

    transition: 0.3s ease-in-out !important;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow: 0px 0px 20px rgba(124,58,237,0.4);
}

/* ======================================================
METRICS
====================================================== */

div[data-testid="metric-container"] {

    background: rgba(17,24,39,0.95);

    border: 1px solid rgba(255,255,255,0.06);

    padding: 1.2rem;

    border-radius: 18px;

    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}

/* ======================================================
METRIC LABELS
====================================================== */

div[data-testid="metric-container"] label {

    color: #9CA3AF !important;

    font-size: 0.95rem !important;
}

/* ======================================================
METRIC VALUES
====================================================== */

div[data-testid="metric-container"] [data-testid="stMetricValue"] {

    color: #4ADE80 !important;

    font-size: 2rem !important;

    font-weight: 700 !important;
}

/* ======================================================
DATAFRAME
====================================================== */

[data-testid="stDataFrame"] {

    background-color: rgba(17,24,39,0.95);

    border-radius: 15px;

    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.08);
}

/* ======================================================
TABS
====================================================== */

.stTabs [role="tab"] {

    color: white !important;

    background-color: #111827 !important;

    border-radius: 10px 10px 0px 0px;

    padding: 10px 20px;

    margin-right: 5px;
}

.stTabs [aria-selected="true"] {

    background-color: #4F46E5 !important;
}

/* ======================================================
INFO/SUCCESS/WARNING BOXES
====================================================== */

.stAlert {

    border-radius: 12px !important;
}

/* ======================================================
SCROLLBAR
====================================================== */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: #111827;
}

::-webkit-scrollbar-thumb {

    background: #4F46E5;

    border-radius: 10px;
}

/* ======================================================
PLOTLY CHART BACKGROUND FIX
====================================================== */

.js-plotly-plot .plotly,
.js-plotly-plot .plot-container {

    background: transparent !important;
}

/* ======================================================
TABLE TEXT VISIBILITY FIX
====================================================== */

table {

    color: white !important;
}

/* ======================================================
MARKDOWN TEXT FIX
====================================================== */

.element-container {

    color: white !important;
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("📊 Clarity Invest Pro Dashboard")

# =========================================================
# HERO SECTION
# =========================================================

st.info(
    "🚀 Beginner-friendly investing dashboard for understanding stocks, trends, and risk in a simplified way."
)

st.markdown(
    """
    ### Simplifying Investing For Beginners
    
    Understand stocks, risk, trends, and investing concepts in a simple and practical way.
    """
)

st.caption(
    "Built to help beginners gain investing clarity through simple insights and practical understanding."
)

st.markdown("---")

# =========================================================
# HOW IT WORKS
# =========================================================

st.header("⚙️ How It Works")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("1️⃣ Analyze")

    st.write(
        "Search companies and understand stock movement, risk, and trends."
    )

with col2:

    st.subheader("2️⃣ Compare")

    st.write(
        "Compare multiple companies side-by-side for better investing clarity."
    )

with col3:

    st.subheader("3️⃣ Learn")

    st.write(
        "Access beginner-friendly investing guidance and personalized clarity support."
    )

st.markdown("---")

# =========================================================
# WHY CLARITY INVEST
# =========================================================

st.header("💡 Why Clarity Invest")

st.write("""
Most beginners feel confused because investing information is often too complicated.

Clarity Invest focuses on:
- Simple explanations
- Beginner-friendly insights
- Risk understanding
- Practical learning
- Long-term clarity over hype
""")

st.markdown("---")

# =========================================================
# FREE FEATURES
# =========================================================

st.header("📊 Free Dashboard Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ Stock Trend Analysis")
    st.success("✅ Risk Analysis")
    st.success("✅ Company Comparison")
    st.success("✅ Interactive Charts")

with col2:

    st.success("✅ Sector Insights")
    st.success("✅ Historical Data")
    st.success("✅ Beginner-Friendly Explanations")
    st.success("✅ Investment Observations")

st.markdown("---")

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
# SAFE COMPANY SEARCH
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
# STOCK NEWS FUNCTION
# =========================================================

def get_stock_news(ticker_symbol):

    try:

        ticker = yf.Ticker(ticker_symbol)

        news = ticker.news

        return news[:5]

    except Exception:

        return []
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
        # FIX MULTIINDEX ISSUE
        # =================================================

        if isinstance(data.columns, pd.MultiIndex):

            data.columns = data.columns.get_level_values(0)

        # =================================================
        # REQUIRED COLUMNS CHECK
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

    except Exception as e:

        st.error(f"Error analyzing {company}")

        st.write(e)

        return None



# =========================================================
# TRUST NOTE
# =========================================================

st.caption("""
⚠️ Educational purpose only.
No guaranteed returns or financial advice.
""")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Clarity Invest")

company = st.sidebar.text_input(
    "Enter Company Name",
    "Reliance"
)

period = st.sidebar.selectbox(

    "Select Investment Period",

    [
        "Short Term",
        "Medium Term",
        "Long Term"
    ]

)

analyze_button = st.sidebar.button(
    "Analyze Stock"
)

# =========================================================
# ANALYSIS SECTION
# =========================================================

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

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Current Price",
            f"₹{result['Current Price']}"
        )

        col2.metric(
            "Price Change %",
            f"{result['Price Change']}%"
        )

        col3.metric(
            "Risk Level",
            result['Risk']
        )

        col4.metric(
            "Trend",
            result['Trend']
        )

        st.markdown("---")

        # =================================================
        # TABS
        # =================================================

        tab1, tab2, tab3, tab4 = st.tabs(

            [
                "📈 Interactive Chart",
                "💡 Insights",
                "📊 Historical Data",
                 "📰 Latest News"
            ]

        )

        # =================================================
        # CHART TAB
        # =================================================

        with tab1:

            data = result['Data']

            fig = make_subplots(

                rows=2,
                cols=1,

                shared_xaxes=True,

                vertical_spacing=0.03,

                row_heights=[0.75, 0.25]

            )

            # =================================================
            # CANDLESTICK
            # =================================================

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

            # =================================================
            # MOVING AVERAGES
            # =================================================

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

            # =================================================
            # VOLUME
            # =================================================

            fig.add_trace(

                go.Bar(

                    x=data.index,
                    y=data['Volume'],

                    name='Volume'

                ),

                row=2,
                col=1

            )

            # =================================================
            # LAYOUT
            # =================================================

            fig.update_layout(

                template="plotly_dark",

                height=750,

                title=f"{result['Company']} Stock Analysis",

                xaxis_rangeslider_visible=False

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        # =================================================
        # INSIGHTS TAB
        # =================================================

        with tab2:

            st.subheader("📌 Company Information")

            st.write(
                f"**Company:** {result['Company']}"
            )

            st.write(
                f"**Ticker:** {result['Ticker']}"
            )

            st.write(
                f"**Sector:** {result['Sector']}"
            )

            st.write(
                f"**Volatility:** {result['Volatility']}"
            )

            st.markdown("---")

            st.subheader("📊 Investment Observation")

            st.info(
                result['Observation']
            )

            st.subheader("💡 Sector Insight")

            st.success(
                result['Sector Insight']
            )

            st.subheader("⚠️ Reminder")

            st.warning(
                "Investment decisions should align with your financial goals and risk comfort."
            )

        # =================================================
        # DATA TAB
        # =================================================

        with tab3:

            st.subheader("📊 Historical Stock Data")

            st.dataframe(

                data.tail(100),

                use_container_width=True

            )

        # =========================================================
        # NEWS ANALYSIS
        # =========================================================

       with tab4:
           st.subheader("📰 Latest Stock News")

        try:
    
            ticker_news = yf.Ticker(result['Ticker'])
    
            news_data = ticker_news.news
    
            if len(news_data) > 0:
    
                for news in news_data[:5]:
    
                    title = news.get("title", "No Title")
    
                    publisher = news.get("publisher", "Unknown")
    
                    link = news.get("link", "")
    
                    thumbnail = news.get("thumbnail")
    
                    st.subheader(title)
    
                    st.write(f"📰 Source: {publisher}")
    
                    if thumbnail:
    
                        try:
    
                            st.image(
                                thumbnail['resolutions'][0]['url'],
                                width=500
                            )
    
                        except:
                            pass
    
                    st.link_button(
                        "Read Full News",
                        link
                    )
    
                    st.markdown("---")
    
            else:
    
                st.info("No recent news available.")
    
        except:
    
            st.warning("Unable to fetch latest news.")
            
# =========================================================
# BUY / HOLD / SELL SENTIMENT
# =========================================================

st.markdown("---")

st.header("🤖 Investment Sentiment")

if analyze_button and result:

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

        sentiment = "📌 HOLD"

    else:

        sentiment = "⚠️ Sell Caution"

    st.subheader(sentiment)

    st.write("""
This sentiment is generated using:
- Trend analysis
- Risk analysis
- Moving averages
- Historical volatility
""")

    st.caption(
        "Educational purpose only. Not financial advice."
    )  

# =========================================================
# SIP CALCULATOR
# =========================================================

st.markdown("---")

st.header("💰 SIP Calculator")

sip_amount = st.number_input(
    "Monthly SIP Amount (₹)",
    min_value=500,
    value=5000
)

years = st.slider(
    "Investment Duration (Years)",
    1,
    30,
    10
)

expected_return = st.slider(
    "Expected Annual Return (%)",
    1,
    30,
    12
)

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

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Invested",
    f"₹{total_invested:,.0f}"
)

col2.metric(
    "Estimated Value",
    f"₹{future_value:,.0f}"
)

col3.metric(
    "Estimated Returns",
    f"₹{wealth_gained:,.0f}"
)

# =========================================================
# PORTFOLIO ALLOCATION TOOL
# =========================================================

st.markdown("---")

st.header("📊 Beginner Portfolio Allocation")

risk_profile = st.selectbox(

    "Select Risk Comfort",

    [
        "Low Risk",
        "Moderate Risk",
        "High Risk"
    ]

)

if risk_profile == "Low Risk":

    st.success("""
✅ Suggested Allocation

• 60% Large Cap Stocks
• 30% Index Funds
• 10% Gold / Cash
""")

elif risk_profile == "Moderate Risk":

    st.info("""
📈 Suggested Allocation

• 50% Large Cap Stocks
• 30% Mid Cap Stocks
• 20% Index Funds
""")

else:

    st.warning("""
🚀 Suggested Allocation

• 50% Growth Stocks
• 30% Mid/Small Cap
• 20% High Risk Opportunities
""")

st.caption(
    "Educational allocation example for beginners."
)

# =========================================================
# COMPARISON SECTION
# =========================================================

st.sidebar.markdown("---")

st.sidebar.subheader("⚖️ Compare Companies")

comparison_input = st.sidebar.multiselect(

    "Select Popular Companies",

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

custom_companies = st.sidebar.text_input(

    "Or Enter Custom Companies (comma separated)",

    ""

)
compare_button = st.sidebar.button(
    "Compare Stocks"
)


# =========================================================
# COMPARISON LOGIC
# =========================================================

if compare_button:

    comparison_results = []

    # Selected companies
    companies = comparison_input.copy()

    # Add custom companies
    if custom_companies:

        custom_list = custom_companies.split(",")

        for comp in custom_list:

            comp = comp.strip()

            if comp and comp not in companies:

                companies.append(comp)

    # No company selected
    if len(companies) == 0:

        st.warning("Please select or enter companies.")

    else:

        with st.spinner("Comparing companies..."):

            for comp in companies:

                result = analyze_stock(
                    comp,
                    period
                )

                if result:

                    comparison_results.append(result)

        # =================================================
        # SHOW RESULTS
        # =================================================

        if len(comparison_results) > 0:

            st.markdown("---")

            st.header("📊 Company Comparison")

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

            # =============================================
            # COMPARISON CHART
            # =============================================

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

                title="Normalized Performance Comparison",

                xaxis_title="Date",

                yaxis_title="Normalized Performance",

                height=650

            )

            st.plotly_chart(
                comparison_fig,
                use_container_width=True
            )

        else:

            st.error(
                "No valid companies found for comparison."
            )
        if len(companies) > 8:

            st.warning("Please compare maximum 8 companies at once.")

            st.stop()

# =========================================================
# PREMIUM CLARITY SECTION
# =========================================================

st.markdown("---")

st.header("🎯 Personalized Beginner Clarity")

st.write("""
Get beginner-friendly investing understanding based on:

• Your goals  
• Risk comfort  
• Budget  
• Investing stage  

Designed for students and beginners looking for clearer financial understanding.
""")

# =========================================================
# SERVICES
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.info("""
📘 Beginner Investing Guide  
₹49
""")

    st.write("""
• Beginner-friendly investing understanding  
• Risk clarity  
• Common beginner mistakes  
• Practical examples  
""")

    # PDF DOWNLOAD
    try:

        with open(
            "Clarity_Invest_Beginner_Guide.pdf",
            "rb"
        ) as pdf_file:

            st.download_button(

                label="📥 Download Guide PDF",

                data=pdf_file,

                file_name="Clarity_Invest_Beginner_Guide.pdf",

                mime="application/pdf"

            )

    except:

        st.warning(
            "PDF guide not uploaded yet."
        )

with col2:

    st.success("""
🎯 Personalized Beginner Clarity  
₹99
""")

    st.write("""
• Personalized beginner guidance  
• Based on your goals & comfort  
• Simplified investing explanation  
• Personal clarity support  
""")

# =========================================================
# MORE SERVICES
# =========================================================

col3, col4 = st.columns(2)

with col3:

    st.warning("""
📊 Portfolio Guidance  
₹199
""")

    st.write("""
• Beginner allocation understanding  
• Risk balance thinking  
• Practical portfolio structure  
""")

with col4:

    st.info("""
📞 1-on-1 Beginner Guidance  
₹299+
""")

    st.write("""
• Direct beginner support  
• Personalized investing discussions  
• Clarity-focused guidance  
""")

# =========================================================
# PAYMENT SECTION
# =========================================================

st.markdown("---")

st.subheader("💳 Payment Process")

st.write("""
1. Complete payment using the QR code  
2. Click the form button below  
3. Fill your investing details  
4. Receive personalized clarity guidance  
""")

# =========================================================
# QR IMAGE
# =========================================================

try:
    st.image("clarity_invest_qr.JPEG", width=250)
except:
    st.warning("QR code not uploaded yet.")

# =========================================================
# GOOGLE FORM BUTTON
# =========================================================

st.link_button(
    "Proceed to Personalized Clarity Form",
    "https://docs.google.com/forms/d/1NxGIVfxyViyLncwt299FWVOxrH5dv5tGjVYz-abg-EM/edit"
)

# =========================================================
# CONTACT SECTION
# =========================================================

st.markdown("---")

st.markdown("""

<div style='text-align:center;'>

<h3>📩 Connect With Clarity Invest</h3>

<p>
Instagram: https://www.instagram.com/clarity_invest_insights?igsh=bXdtMHk0Mzh1Zmpj
</p>

<p>
LinkedIn: https://www.linkedin.com/in/gauri-ganorkar-278260344/
</p>

<p>
For personalized investing clarity and beginner guidance.
</p>

</div>

""", unsafe_allow_html=True)
# =========================================================
# TRUST SECTION
# =========================================================

st.markdown("---")

st.header("🤝 Beginner-Focused Investing")

st.write("""
Clarity Invest is designed for educational and informational purposes.

The goal is not to provide stock tips or guaranteed returns.

The focus is:
- Understanding investing
- Learning risk management
- Building financial clarity
- Making informed decisions
""")

# =========================================================
# DISCLAIMER
# =========================================================

st.markdown("---")

st.caption("""
Disclaimer:
This platform is built for educational and informational purposes only.
It does not provide financial advice, stock recommendations, or guaranteed returns.
Please do your own research before making investment decisions.
""")

st.markdown("""
<div style='text-align:center; color:#9CA3AF;'>

Clarity Invest • Beginner Financial Understanding Platform

Designed to simplify investing concepts for students and first-time investors.

</div>
""", unsafe_allow_html=True)
