import streamlit as st
import yfinance as yf
import feedparser
import urllib.parse
from datetime import datetime

# =========================================================
# CACHE: COMPANY NAME
# =========================================================
@st.cache_data(ttl=3600)
def get_company_name(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        return info.get("longName") or ticker_symbol
    except:
        return ticker_symbol


# =========================================================
# SMART NEWS FETCHER (Google News RSS)
# =========================================================
@st.cache_data(ttl=600)
def fetch_news(query):
    encoded_query = urllib.parse.quote(query)

    url = (
        f"https://news.google.com/rss/search?q={encoded_query}"
        f"&hl=en-IN&gl=IN&ceid=IN:en"
    )

    feed = feedparser.parse(url)

    news_items = []

    for entry in feed.entries[:10]:

        title = entry.get("title", "No Title")
        link = entry.get("link", "")
        published = entry.get("published", "Unknown date")

        source = "Google News"
        if "source" in entry and isinstance(entry.source, dict):
            source = entry.source.get("title", "Google News")

        news_items.append({
            "title": title,
            "link": link,
            "publisher": source,
            "published": published
        })

    return news_items


# =========================================================
# HEADER UI
# =========================================================
def render_header(company_name):

    st.markdown(f"""
    <div style="
        padding:28px;
        border-radius:18px;
        background: linear-gradient(135deg,#0F172A,#1E293B,#312E81);
        color:white;
        margin-bottom:20px;
        box-shadow:0 10px 30px rgba(0,0,0,0.3);
    ">
        <h1 style="margin-bottom:5px;">📰 Latest Market News</h1>
        <h3 style="margin-bottom:5px;">{company_name}</h3>
        <p style="opacity:0.8;">Real-time curated financial news for better investing decisions</p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# NEWS CARD UI
# =========================================================
def render_news_card(news):

    st.markdown("""
    <div style="
        padding:18px;
        border-radius:14px;
        background:#0B1220;
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:12px;
    ">
    """, unsafe_allow_html=True)

    st.markdown(f"### {news['title']}")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.caption(f"🗞️ {news['publisher']}")

    with col2:
        st.caption(f"📅 {news['published']}")

    if news["link"]:
        st.link_button("🔗 Open Full Article", news["link"])

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# MAIN NEWS SECTION
# =========================================================
def show_news_section(ticker_symbol):

    company_name = get_company_name(ticker_symbol)

    render_header(company_name)

    # =====================================================
    # SMART QUERY STRATEGY
    # =====================================================
    queries = [
        company_name,
        f"{company_name} stock",
        f"{company_name} earnings",
        f"{company_name} financial results",
    ]

    all_news = []

    for q in queries:
        all_news.extend(fetch_news(q))

    # Remove duplicates (by title)
    seen = set()
    unique_news = []

    for n in all_news:
        if n["title"] not in seen:
            unique_news.append(n)
            seen.add(n["title"])

    # =====================================================
    # EMPTY STATE
    # =====================================================
    if not unique_news:
        st.warning("No news found for this company right now.")
        return

    # =====================================================
    # NEWS UI SECTION
    # =====================================================
    st.subheader("📌 Top Market Updates")

    for news in unique_news[:12]:
        render_news_card(news)

    # =====================================================
    # EDUCATIONAL LAYER (IMPORTANT FOR BEGINNERS)
    # =====================================================
    st.markdown("---")

    with st.expander("📘 How to read this news (Beginner Guide)"):

        st.markdown("""
        - Don’t react to a single headline  
        - Look for repeated themes (earnings, debt, growth)  
        - Compare news with stock price movement  
        - Check if news is short-term noise or long-term impact  
        - Always verify with financial statements  

        👉 Good investors read *patterns*, not headlines.
        """)

    st.info("📊 This news is for educational purposes only. Not financial advice.")