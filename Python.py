'''import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import search

print("\n========== CLARITY INVEST ANALYSIS ==========\n")

# User Input
company = input("Enter company name: ")
print("\n")

try:
    # Search Company Ticker
    result = search(company)

    # Extract ticker symbol
    stock = result['quotes'][0]['symbol']

    print(f"Ticker Found: {stock}")
    print("\n")

    # Investment Period
    period = input("Choose investment period (short / medium / long): ").lower()
    print("\n")

    if period == "short":
        start_date = "2025-01-01"

    elif period == "medium":
        start_date = "2024-01-01"

    elif period == "long":
        start_date = "2020-01-01"

    else:
        print("Invalid option selected.")
        exit()

    # Download Stock Data
    data = yf.download(stock, start=start_date)

    # Check if data exists
    if data.empty:
        print("No stock data found.")
        exit()

    # Calculate Returns
    data['Returns'] = data['Close'].pct_change()

    # Current Price
    current_price = data['Close'].iloc[-1]

    print("========== STOCK SUMMARY ==========\n")

    print(f"Current Price: ₹{round(current_price, 2)}")
    print("\n")

    # Volatility Calculation
    volatility = data['Returns'].std()

    # Risk Level
    if volatility < 0.02:
        risk = "Low Risk / Beginner Friendly"

    elif volatility < 0.05:
        risk = "Moderate Risk"

    else:
        risk = "High Risk"

    print(f"Risk Level: {risk}")
    print("\n")

    print(f"Volatility: {round(volatility, 4)}")
    print("\n")

    # Volatility Explanation
    print("Volatility Explanation:")
    print("This stock shows price fluctuations over time.")
    print("Higher volatility generally means higher risk and uncertainty.")
    print("\n")

    # Moving Averages
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()

    # Trend Logic
    if data['MA50'].iloc[-1] > data['MA200'].iloc[-1]:

        trend = "Positive Trend"

        explanation = (
            "The stock is showing stronger recent momentum "
            "compared to its long-term average."
        )

    else:

        trend = "Weak Trend"

        explanation = (
            "The stock is currently showing weaker recent movement "
            "compared to its long-term average."
        )

    print(f"Trend: {trend}")
    print("\n")

    print("Trend Explanation:")
    print(explanation)
    print("\n")

    # Chart Explanation
    print("How To Read The Chart:")
    print("• Blue line shows actual stock price movement.")
    print("• Orange line shows short-term average trend.")
    print("• Green line shows long-term average trend.")
    print("• If orange stays above green, momentum may be positive.")
    print("\n")

    print("Reminder:")
    print("Investing decisions should align with your personal risk comfort and financial goals.")
    print("\n")

    # Plot Chart
    plt.figure(figsize=(12, 6))

    plt.plot(data['Close'], label="Stock Price")
    plt.plot(data['MA50'], label="50-Day Moving Average")
    plt.plot(data['MA200'], label="200-Day Moving Average")

    plt.title(f"{company.title()} Stock Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()

    plt.show()

except:
    print("Company not found or invalid data received.")

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import search

# -----------------------------------
# CHART STYLE
# -----------------------------------

plt.style.use("ggplot")

print("\n========== CLARITY INVEST ANALYSIS ==========\n")

# -----------------------------------
# FUNCTION TO ANALYZE STOCK
# -----------------------------------

def analyze_stock(company, period):

    try:

        # -----------------------------------
        # SEARCH COMPANY
        # -----------------------------------

        result = search(company)

        if 'quotes' not in result or len(result['quotes']) == 0:

            print(f"Company not found: {company}")
            return None

        quotes = result['quotes']

        stock = None

        # Prefer NSE Stocks
        for q in quotes:

            symbol = q.get('symbol', '')

            if symbol.endswith(".NS"):

                stock = symbol
                break

        # Fallback
        if stock is None:

            for q in quotes:

                symbol = q.get('symbol', '')

                if symbol.endswith(".BO"):

                    stock = symbol
                    break

        # Final fallback
        if stock is None:

            stock = quotes[0]['symbol']

        # -----------------------------------
        # PERIOD SELECTION
        # -----------------------------------

        if period == "short":

            period_value = "6mo"

        elif period == "medium":

            period_value = "1y"

        elif period == "long":

            period_value = "5y"

        else:

            print("Invalid investment period.")
            return None

        # -----------------------------------
        # DOWNLOAD STOCK DATA
        # -----------------------------------

        data = yf.download(
            stock,
            period=period_value,
            auto_adjust=True,
            progress=False
        )

        # -----------------------------------
        # FIX MULTI-INDEX COLUMNS
        # -----------------------------------

        if isinstance(data.columns, pd.MultiIndex):

            data.columns = data.columns.get_level_values(0)

        # -----------------------------------
        # CHECK DATA
        # -----------------------------------

        if data.empty:

            print(f"No stock data found for {company}")
            return None

        # -----------------------------------
        # CLOSE PRICE SERIES
        # -----------------------------------

        close_prices = data['Close'].squeeze()

        # -----------------------------------
        # GET COMPANY INFO
        # -----------------------------------

        try:

            ticker = yf.Ticker(stock)

            info = ticker.info

            sector = info.get("sector", "Other")

        except:

            sector = "Other"

        # -----------------------------------
        # RETURNS
        # -----------------------------------

        data['Returns'] = close_prices.pct_change()

        # -----------------------------------
        # PRICE CALCULATIONS
        # -----------------------------------

        current_price = float(close_prices.iloc[-1])

        start_price = float(close_prices.iloc[0])

        end_price = float(close_prices.iloc[-1])

        change_percent = (
            (end_price - start_price)
            / start_price                                       #p
        ) * 100

        # -----------------------------------
        # VOLATILITY
        # -----------------------------------

        volatility = float(
            data['Returns'].std()                               #p
        )

        # -----------------------------------
        # RISK ANALYSIS
        # -----------------------------------

        if volatility < 0.02:

            risk = "Low Risk"

            beginner_note = (                                    #p
                "Comparatively stable for beginners."
            )

        elif volatility < 0.05:

            risk = "Moderate Risk"

            beginner_note = (
                "Requires moderate market understanding."
            )

        else:

            risk = "High Risk"

            beginner_note = (
                "May fluctuate heavily for beginners."
            )

        # -----------------------------------
        # MOVING AVERAGES
        # -----------------------------------

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

        # -----------------------------------
        # TREND ANALYSIS
        # -----------------------------------

        if period == "short":

            latest_price = close_prices.iloc[-1]

            ma20 = data['MA20'].iloc[-1]

            if latest_price > ma20:

                trend = "Positive Short-Term Trend"

            else:

                trend = "Weak Short-Term Trend"

        elif period == "medium":

            ma20 = data['MA20'].iloc[-1]

            ma50 = data['MA50'].iloc[-1]

            if pd.isna(ma50):

                trend = "Insufficient Data"                             #p

            elif ma20 > ma50:

                trend = "Positive Medium-Term Trend"

            else:

                trend = "Weak Medium-Term Trend"

        elif period == "long":

            ma50 = data['MA50'].iloc[-1]

            ma200 = data['MA200'].iloc[-1]

            if pd.isna(ma200):

                trend = "Insufficient Data"

            elif ma50 > ma200:

                trend = "Positive Long-Term Trend"

            else:

                trend = "Weak Long-Term Trend"
               
        # -----------------------------------
        # INVESTMENT OBSERVATION
        # -----------------------------------

        if change_percent > 20:

            observation = (
                "The company has shown strong growth during this investment period."
            )

        elif change_percent > 0:

            observation = (
                "The company has shown stable positive movement."
            )

        elif change_percent > -10:

            observation = (
                "The company has shown slight negative movement and requires observation."
            )

        else:

            observation = (
                "The company has shown weak performance during this period."
            )

        # -----------------------------------
        # SECTOR INSIGHT
        # -----------------------------------

        if sector == "Technology":

            if trend == "Positive Trend":

                sector_explanation = (
                    "Technology sector is showing positive momentum supported by digital demand."
                )

            else:

                sector_explanation = (
                    "Technology sector is currently showing weaker movement and higher fluctuations."
                )

        elif sector == "Financial Services":

            if trend == "Positive Trend":

                sector_explanation = (
                    "Financial companies are showing positive movement supported by market confidence."
                )

            else:

                sector_explanation = (
                    "Financial companies are currently affected by uncertain economic conditions."
                )

        elif sector == "Healthcare":

            if trend == "Positive Trend":

                sector_explanation = (
                    "Healthcare companies are showing positive movement supported by medical demand."
                )

            else:

                sector_explanation = (
                    "Healthcare companies are currently showing weaker movement despite stable demand."
                )

        elif sector == "Energy":

            if trend == "Positive Trend":

                sector_explanation = (
                    "Energy companies are benefiting from positive fuel demand and market conditions."
                )

            else:

                sector_explanation = (
                    "Energy companies are currently affected by fuel price fluctuations."
                )

        elif sector == "Industrials":

            if trend == "Positive Trend":

                sector_explanation = (
                    "Industrial companies are showing positive movement supported by infrastructure activity."
                )

            else:

                sector_explanation = (
                    "Industrial companies are currently affected by slower business activity."
                )

        elif sector == "Consumer Defensive":

            sector_explanation = (
                "Consumer defensive companies are generally considered stable investments."
            )

        elif sector == "Consumer Cyclical":

            sector_explanation = (
                "Consumer-focused companies are affected by market demand and spending behavior."
            )

        elif (
            "Transportation" in sector
            or "Air" in sector
        ):

            sector_explanation = (
                "Transportation companies are influenced by travel demand and fuel costs."
            )

        elif "Rail" in sector:

            sector_explanation = (
                "Railway companies benefit from transportation and infrastructure demand."
            )

        else:

            sector_explanation = (
                "This sector reacts to broader market and economic conditions."
            )

        # -----------------------------------
        # RETURN RESULTS
        # -----------------------------------

        return {

            "Company": company.title(),
            "Ticker": stock,
            "Sector": sector,
            "Current Price": round(current_price, 2),
            "Price Change %": round(change_percent, 2),
            "Risk": risk,
            "Trend": trend,
            "Volatility": round(volatility, 4),
            "Observation": observation,
            "Beginner Note": beginner_note,
            "Sector Insight": sector_explanation,
            "Data": data
        }

    except Exception as e:

        print(f"\nError analyzing {company}")
        print(f"Reason: {e}")

        return None


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------

company = input(
    "Enter company name: "
)

print("\n")

period = input(
    "Choose investment period (short / medium / long): "
).lower()

print("\n")

result = analyze_stock(company, period)

# -----------------------------------
# DISPLAY RESULT
# -----------------------------------

if result:

    print("========== COMPANY INFORMATION ==========\n")

    print(f"Company: {result['Company']}")
    print("\n")

    print(f"Ticker: {result['Ticker']}")
    print("\n")

    print(f"Company Sector: {result['Sector']}")
    print("\n")

    print(f"Current Price: ₹{result['Current Price']}")
    print("\n")

    print(f"Price Change: {result['Price Change %']}%")
    print("\n")

    print(f"Risk Level: {result['Risk']}")
    print("\n")

    print(f"Trend: {result['Trend']}")
    print("\n")

    print("Investment Observation:")
    print(result['Observation'])
    print("\n")

    print("Beginner Insight:")
    print(result['Beginner Note'])
    print("\n")

    print("Sector Insight:")
    print(result['Sector Insight'])
    print("\n")

    print("How To Read The Chart:")
    print("• Blue line shows actual stock price movement.")
    print("• Orange line shows short-term average trend.")
    print("• Green line shows long-term average trend.")
    print("• If orange stays above green, momentum may be positive.")
    print("\n")

    print("Reminder:")
    print(
        "Investing decisions should align with your financial goals and risk comfort."
    )

    print("\n")

    # -----------------------------------
    # STOCK CHART
    # -----------------------------------

    data = result['Data']

    plt.figure(figsize=(12, 6))

    plt.plot(
        data.index,
        data['Close'],
        label="Stock Price"
    )

    plt.plot(
    data.index,
    data['MA20'],
    label="20-Day MA"
    )

    plt.plot(
        data.index,
        data['MA50'],
        label="50-Day MA"
    )

    plt.plot(
        data.index,
        data['MA200'],
        label="200-Day MA"
    )
    plt.title(
        f"{company.title()} Stock Analysis"
    )

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)


# -----------------------------------
# COMPARISON SECTION
# -----------------------------------

compare = input(
    "Do you want company comparison? (yes/no): "
).lower()

# -----------------------------------
# COMPANY COMPARISON
# -----------------------------------

if compare == "yes":

    print("\n")

    companies = input(
        "Enter company names separated by commas: "
    ).split(",")

    print("\n========== COMPARISON ANALYSIS ==========\n")

    comparison_results = []

    for comp in companies:

        comp = comp.strip()

        result = analyze_stock(
            comp,
            period
        )

        if result:

            comparison_results.append(result)

    # -----------------------------------
    # PRINT COMPARISON
    # -----------------------------------

    for result in comparison_results:

        print("-----------------------------------")

        print(f"Company: {result['Company']}")

        print("-----------------------------------")

        print(f"Ticker: {result['Ticker']}")
        print(f"Sector: {result['Sector']}")
        print(f"Current Price: ₹{result['Current Price']}")
        print(f"Price Change: {result['Price Change %']}%")
        print(f"Risk Level: {result['Risk']}")
        print(f"Trend: {result['Trend']}")

        print("\nInvestment Observation:")
        print(result['Observation'])

        print("\nBeginner Insight:")
        print(result['Beginner Note'])

        print("\nSector Insight:")
        print(result['Sector Insight'])

        print("\n")

    # -----------------------------------
    # COMPARISON CHART
    # -----------------------------------

    if len(comparison_results) > 0:

        plt.figure(figsize=(12, 6))

        for result in comparison_results:

            data = result['Data']

            normalized = (
                data['Close']
                / data['Close'].iloc[0]
            ) * 100

            plt.plot(
                data.index,
                normalized,
                label=result['Company']
            )

        plt.title(
            "Company Comparison (Normalized Performance)"
        )

        plt.xlabel("Date")

        plt.ylabel(
            "Normalized Price (Base = 100)"
        )

        plt.legend()

        plt.grid(True)

        plt.show()

    else:

        print(
            "\nThank you for using Clarity Invest Analysis.\n"
        )
        print("\nSector Insight:")
        print(result['Sector Insight'])

        print("\n")

    # Comparison Chart
    if len(comparison_results) > 0:

        plt.figure(figsize=(12, 6))

        for result in comparison_results:

            data = result['Data']

            plt.plot(
                data['Close'],
                label=result['Company']
            )

        plt.title("Company Comparison")

        plt.xlabel("Date")
        plt.ylabel("Price")

        plt.legend()

        plt.show()


    plt.show()
'''


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

.stTextInput input,
.stSelectbox select,
.stTextArea textarea {

   .stSelectbox div[data-baseweb="select"] > div {

    background-color: #111827 !important;

    color: white !important;

    border: 1px solid #374151 !important;

    border-radius: 12px !important;

    padding: 10px !important;

    /* DROPDOWN MENU */

ul {
    background-color: #111827 !important;
}

li {
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

st.markdown(
    "<h4 style='color:#9CA3AF;'>Professional AI-powered stock analysis platform</h4>",
    unsafe_allow_html=True
)

st.markdown("""
Professional Stock Analysis Dashboard with:
- Technical Indicators
- Risk Analysis
- Trend Analysis
- Sector Insights
- Company Comparison
- Interactive Charts
""")

# =========================================================
# SECTOR INSIGHT FUNCTION
# =========================================================

def get_sector_insight(sector, trend):

    insights = {


    "Technology": {

        "Positive Trend":
            "Technology sector is benefiting from digital transformation and innovation demand.",

        "Weak Trend":
            "Technology sector is currently facing weaker momentum and market volatility."
    },

    "Financial Services": {

        "Positive Trend":
            "Financial companies are benefiting from stronger market confidence and lending activity.",

        "Weak Trend":
            "Financial sector is currently impacted by economic uncertainty and interest rate pressure."
    },

    "Energy": {

        "Positive Trend":
            "Energy companies are benefiting from stronger fuel demand and pricing conditions.",

        "Weak Trend":
            "Energy companies are facing pressure from oil price fluctuations."
    },

    "Healthcare": {

        "Positive Trend":
            "Healthcare sector remains supported by stable medical demand.",

        "Weak Trend":
            "Healthcare companies remain relatively defensive despite weaker momentum."
    },

    "Industrials": {

        "Positive Trend":
            "Industrial companies are benefiting from infrastructure and manufacturing activity.",

        "Weak Trend":
            "Industrial sector is facing slower economic activity."
    },

    "Consumer Defensive": {

        "Positive Trend":
            "Consumer defensive companies are showing stable long-term demand.",

        "Weak Trend":
            "Consumer defensive sector remains comparatively resilient."
    },

    "Consumer Cyclical": {

        "Positive Trend":
            "Consumer-focused companies are benefiting from stronger consumer demand.",

        "Weak Trend":
            "Changing consumer spending patterns are affecting cyclical demand."
    },

    "Transportation": {

        "Positive Trend":
            "Transportation companies are benefiting from stronger logistics demand.",

        "Weak Trend":
            "Transportation sector is facing operational and fuel-cost pressures."
    },

    "Communication Services": {

        "Positive Trend":
            "Communication companies are benefiting from rising digital connectivity demand.",

        "Weak Trend":
            "Communication sector is facing stronger competition and slower momentum."
    },

    "Utilities": {

        "Positive Trend":
            "Utility companies are benefiting from stable infrastructure demand.",

        "Weak Trend":
            "Utilities sector remains comparatively defensive despite weaker momentum."
    },

    "Basic Materials": {

        "Positive Trend":
            "Basic materials companies are benefiting from industrial and construction demand.",

        "Weak Trend":
            "Commodity price fluctuations are affecting the materials sector."
    },

    "Real Estate": {

        "Positive Trend":
            "Real estate companies are benefiting from stronger property and infrastructure activity.",

        "Weak Trend":
            "Real estate sector is facing pressure from interest rates and slower demand."
    },

    "Utilities": {

        "Positive Trend":
            "Utilities sector is benefiting from stable energy and infrastructure demand.",

        "Weak Trend":
            "Utilities remain comparatively stable despite slower growth."
    },

    "Consumer Staples": {

        "Positive Trend":
            "Consumer staples companies are supported by stable daily consumption demand.",

        "Weak Trend":
            "Consumer staples sector remains relatively defensive in weaker markets."
    },

    "Communication": {

        "Positive Trend":
            "Communication companies are benefiting from growing media and connectivity demand.",

        "Weak Trend":
            "Communication sector is facing competitive and advertising pressures."
    },

    "Real Estate Services": {

        "Positive Trend":
            "Real estate services are benefiting from improving property market activity.",

        "Weak Trend":
            "Property-related businesses are currently facing slower market movement."
    },

    "Airlines": {

        "Positive Trend":
            "Airline companies are benefiting from stronger travel demand and tourism activity.",

        "Weak Trend":
            "Airline companies are affected by fuel price volatility and changing travel demand."
    },

    "Railroads": {

        "Positive Trend":
            "Railway companies are benefiting from transportation and infrastructure growth.",

        "Weak Trend":
            "Railway companies are currently facing slower industrial movement."
    },

    "Auto Manufacturers": {

        "Positive Trend":
            "Automobile companies are benefiting from rising consumer and EV demand.",

        "Weak Trend":
            "Auto companies are facing supply-chain and demand-related pressures."
    },

    "Banks": {

        "Positive Trend":
            "Banks are benefiting from lending growth and economic activity.",

        "Weak Trend":
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

    elif trend == "Weak Trend" and risk == "Low Risk":

        return (
            "Stock remains stable, but momentum is currently limited."
        )

    elif trend == "Weak Trend" and risk == "Moderate Risk":

        return (
            "Moderate volatility with weaker momentum currently."
        )

    elif trend == "Weak Trend" and risk == "High Risk":

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

    except:

        return None

# =========================================================
# MAIN ANALYSIS FUNCTION
# =========================================================

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

                trend = "Weak Trend"

        elif period == "Medium Term":

            if pd.isna(ma20) or pd.isna(ma50):

                trend = "Insufficient Data"

            elif ma20 > ma50:

                trend = "Positive Trend"

            else:

                trend = "Weak Trend"

        else:

            if pd.isna(ma50) or pd.isna(ma200):

                trend = "Insufficient Data"

            elif ma50 > ma200:

                trend = "Positive Trend"

            else:

                trend = "Weak Trend"

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

        except:

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

        tab1, tab2, tab3 = st.tabs(

            [
                "📈 Interactive Chart",
                "💡 Insights",
                "📊 Historical Data"
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

    else:

        st.error(
            "Company not found or data unavailable."
        )

# =========================================================
# COMPARISON SECTION
# =========================================================

st.sidebar.markdown("---")

st.sidebar.subheader("⚖️ Compare Companies")

comparison_input = st.sidebar.text_area(

    "Enter company names separated by commas",

    "Reliance, Infosys"

)

compare_button = st.sidebar.button(
    "Compare Stocks"
)

# =========================================================
# COMPARISON LOGIC
# =========================================================

if compare_button:

    comparison_results = []

    companies = comparison_input.split(",")

    with st.spinner("Comparing companies..."):

        for comp in companies:

            comp = comp.strip()

            result = analyze_stock(
                comp,
                period
            )

            if result:

                comparison_results.append(
                    result
                )

    if len(comparison_results) > 0:

        st.markdown("---")

        st.header("📊 Company Comparison")

        # =================================================
        # COMPARISON TABLE
        # =================================================

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

        # =================================================
        # NORMALIZED COMPARISON CHART
        # =================================================

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
