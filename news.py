# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import yfinance as yf

# =========================================================
# NEWS FUNCTION
# =========================================================

def show_news_section(ticker_symbol):

    # =====================================================
    # SECTION HEADER
    # =====================================================

    st.markdown(
        """
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
📰 Latest Market News
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:15px;
'>
Stay updated with recent company-related developments
</h3>

<p style='
color:#CBD5E1;
font-size:17px;
line-height:1.8;
'>
Understand market developments, company activity, and news events in a beginner-friendly way.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.info(
        """
News can influence:
        
✅ stock movement  
✅ investor sentiment  
✅ sector trends  
✅ market volatility  
✅ company perception  
"""
    )

    st.markdown("---")

    # =====================================================
    # FETCH NEWS
    # =====================================================

    try:

        ticker = yf.Ticker(ticker_symbol)

        news_data = ticker.news

        # =================================================
        # NO NEWS
        # =================================================

        if not news_data or len(news_data) == 0:

            st.warning(
                "No recent news available for this company."
            )

            return

        # =================================================
        # NEWS LOOP
        # =================================================

        for news in news_data[:5]:

            title = news.get(
                "title",
                "No Title"
            )

            publisher = news.get(
                "publisher",
                "Unknown Source"
            )

            link = news.get(
                "link",
                ""
            )

            thumbnail = news.get(
                "thumbnail"
            )

            # =============================================
            # NEWS CARD
            # =============================================

            st.markdown(
                """
<div style='
padding:22px;
border-radius:20px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
margin-bottom:25px;
'>
""",
                unsafe_allow_html=True
            )

            # =============================================
            # TITLE
            # =============================================

            st.subheader(title)

            # =============================================
            # SOURCE
            # =============================================

            st.caption(f"📰 Source: {publisher}")

            # =============================================
            # IMAGE
            # =============================================

            if thumbnail:

                try:

                    image_url = thumbnail[
                        'resolutions'
                    ][0]['url']

                    st.image(
                        image_url,
                        use_container_width=True
                    )

                except Exception:

                    pass

            # =============================================
            # LINK BUTTON
            # =============================================

            if link:

                st.link_button(
                    "🔗 Read Full News",
                    link,
                    use_container_width=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

        # =================================================
        # BEGINNER LEARNING SECTION
        # =================================================

        st.markdown("---")

        st.subheader("📚 Beginner Market Understanding")

        st.write(
            """
News may impact companies differently depending on:
            
- company performance
- investor expectations
- economic conditions
- market sentiment
- sector activity

Beginner investors should focus on understanding the broader context instead of reacting emotionally to short-term headlines.
"""
        )

        # =================================================
        # IMPORTANT REMINDER
        # =================================================

        st.markdown("---")

        st.warning(
            """
⚠️ Important Reminder:
            
News alone should not determine investment decisions.
            
Long-term investing understanding, risk management, and research are important for informed decision-making.
"""
        )

    # =====================================================
    # ERROR HANDLING
    # =====================================================

    except Exception:

        st.error(
            "Unable to fetch latest market news currently."
        )

    # =====================================================
    # PREMIUM CTA
    # =====================================================

    st.markdown("---")

    st.subheader("🎯 Want Beginner-Friendly Market Guidance?")

    st.markdown(
        """
<div style='
padding:25px;
border-radius:20px;
background: linear-gradient(135deg,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.06);
'>

<h3 style='color:white;'>
Get Personalized Beginner Clarity
</h3>

<p style='color:#E5E7EB;font-size:17px;'>

Understand:
        
✅ market behavior  
✅ beginner investing  
✅ risk understanding  
✅ stock analysis basics  
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