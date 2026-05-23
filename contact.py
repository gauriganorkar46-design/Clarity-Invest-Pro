# =========================================================
# IMPORTS
# =========================================================

import streamlit as st

# =========================================================
# CONTACT PAGE
# =========================================================

def show_contact_page():

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
📩 Connect With Clarity Invest
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Beginner-focused investing guidance platform
</h3>

<p style='
color:#CBD5E1;
font-size:22px;
line-height:1.8;
'>
Connect for beginner-friendly investing understanding, financial clarity, and educational guidance.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    # =====================================================
    # CONTACT CARDS
    # =====================================================

    col1, col2 = st.columns(2)

    # =====================================================
    # INSTAGRAM
    # =====================================================

    with col1:

        st.markdown(
            """
<div class='custom-card'>

<h2>
📸 Instagram
</h2>

<p>

Follow Clarity Invest for:
<br><br>

✅ investing content  
✅ beginner explanations  
✅ stock understanding  
✅ finance insights  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.link_button(

            "Open Instagram",

            "https://www.instagram.com/clarity_invest_insights?igsh=bXdtMHk0Mzh1Zmpj",

            use_container_width=True

        )

    # =====================================================
    # LINKEDIN
    # =====================================================

    with col2:

        st.markdown(
            """
<div class='custom-card'>

<h2>
💼 LinkedIn
</h2>

<p>

Connect professionally for:
<br><br>

✅ finance + tech projects  
✅ investing learning  
✅ student networking  
✅ professional updates  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.link_button(

            "Open LinkedIn",

            "https://www.linkedin.com/in/gauri-ganorkar-278260344/",

            use_container_width=True

        )

    st.markdown("---")

    # =====================================================
    # BEGINNER MESSAGE
    # =====================================================

    st.markdown(
        """
<div style='
padding:30px;
border-radius:24px;
background: linear-gradient(135deg,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.06);
'>

<h2 style='color:white;'>
🎯 Built For Beginners
</h2>

<p style='
color:#E5E7EB;
font-size:25px;
line-height:1.9;
'>

Clarity Invest focuses on simplifying investing concepts for students and beginners who want practical understanding instead of complicated finance language.

</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.caption(
        """
Educational purpose only.
No guaranteed returns or financial advice.
"""
    )