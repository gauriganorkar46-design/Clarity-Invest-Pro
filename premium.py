# =========================================================
# IMPORTS
# =========================================================

import streamlit as st

# =========================================================
# PREMIUM PAGE
# =========================================================

def show_premium_page():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
<div style='
padding:40px;
border-radius:28px;
background: linear-gradient(135deg,#1E1B4B,#312E81,#581C87);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:25px;
'>

<h1 style='
color:white;
font-size:50px;
font-weight:800;
margin-bottom:10px;
'>
🪄 Personalized Beginner Guidance
</h1>

<h3 style='
color:#D1D5DB;
font-weight:400;
margin-bottom:20px;
'>
Designed for students and beginner investors
</h3>

<p style='
color:#C4B5FD;
font-size:28px;
line-height:1.5;
'>
Understand investing in a simplified and beginner-friendly way with personalized clarity support.
</p>

</div>
""",
        unsafe_allow_html=True
    )

    # =====================================================
    # WHY PREMIUM
    # =====================================================

    st.subheader("💡 Why Beginners Prefer Personalized Guidance")

    st.info(
        """
Most beginners struggle because:

- Too much confusing information online
- Difficulty understanding risk
- No clarity on where to start
- Fear of making mistakes
- Lack of practical investing understanding

This premium section focuses on:
        
✅ Beginner-friendly clarity  
✅ Simplified explanations  
✅ Personalized understanding  
✅ Practical learning  
✅ Risk awareness  
"""
    )

    st.markdown("---")

    # =====================================================
    # SERVICES SECTION
    # =====================================================

    st.subheader("💎 Premium Services")

    # =====================================================
    # ROW 1
    # =====================================================

    col1, col2 = st.columns(2)

    # =====================================================
    # BEGINNER GUIDE
    # =====================================================

    with col1:

        st.markdown(
            """
<div style='
padding:30px;
border-radius:22px;
background: rgba(15,23,42,0.92);
border:1px solid rgba(255,255,255,0.06);
display:flex;
flex-direction:column;
justify-content:space-between;
min-height:320px;
'>

<h2 style='color:white;'>
📘 Beginner Investing Guide
</h2>

<h1 style='color:#4ADE80;'>
₹49
</h1>

<p style='color:#D1D5DB;
font-size:16px;
line-height:1.8;
margin-top:15px;
'>

✔ Investing basics  
✔ Risk understanding  
✔ Common beginner mistakes  
✔ Long-term investing mindset  
✔ Beginner-friendly explanations  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown("")

        try:

            with open(
                "Clarity_Invest_Beginner_Guide.pdf",
                "rb"
            ) as pdf_file:

                st.download_button(

                    label="📥 Download Beginner Guide",

                    data=pdf_file,

                    file_name="Clarity_Invest_Beginner_Guide.pdf",

                    mime="application/pdf",

                )

        except:

            st.warning(
                "Beginner guide PDF not uploaded yet."
            )

    # =====================================================
    # PERSONALIZED GUIDANCE
    # =====================================================

    with col2:

        st.markdown(
            """
<div class='premium-card' style='
padding:30px;
border-radius:22px;
background: rgba(15,23,42,0.92);
border:1px solid rgba(255,255,255,0.06);
display:flex;
flex-direction:column;
justify-content:space-between;
height:320px;
'>

<h2 style='color:white;'>
🎯 Personalized Beginner Clarity
</h2>

<h1 style='color:#FBBF24;'>
₹99
</h1>

<p style='color:#E5E7EB;
font-size:16px;
line-height:1.8;
margin-top:15px;'>

✔ Personalized beginner guidance  
✔ Based on your goals  
✔ Based on your comfort level  
✔ Simplified investing explanation  
✔ Beginner-focused investing clarity  

</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown("")

        personalized_clicked = st.button(
            "🚀 Get Personalized Guidance",
            use_container_width=True
        )

    # =====================================================
    # ROW 2
    # =====================================================

    st.markdown("")

    col3, col4 = st.columns(2)

    # =====================================================
    # PORTFOLIO GUIDANCE
    # =====================================================

    with col3:

        st.markdown(
            """
<div class='premium-card' style='
padding:30px;
border-radius:22px;
background: rgba(15,23,42,0.92);
border:1px solid rgba(255,255,255,0.06);
display:flex;
flex-direction:column;
justify-content:space-between;
min-height:320px;
'>

<h2 style='color:white;'>
💹 Portfolio Guidance
</h2>

<h1 style='color:#60A5FA;'>
₹199
</h1>

<p style='color:#D1D5DB;
font-size:16px;
line-height:1.8;
margin-top:15px;'>

✔ Beginner portfolio understanding  
✔ Allocation clarity  
✔ Risk balance understanding  
✔ Long-term investing thinking  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # 1-ON-1 GUIDANCE
    # =====================================================

    with col4:

        st.markdown(
            """
<div class='premium-card' style='
padding:30px;
border-radius:22px;
background: rgba(15,23,42,0.92);
border:1px solid rgba(255,255,255,0.06);
display:flex;
flex-direction:column;
justify-content:space-between;
min-height:320px;
'>

<h2 style='color:white;'>
📞 1-on-1 Beginner Guidance
</h2>

<h1 style='color:#F87171;'>
₹299+
</h1>

<p style='color:#D1D5DB;
font-size:16px;
line-height:1.8;
margin-top:15px;
'>

✔ Direct beginner support  
✔ Investing clarity discussions  
✔ Beginner Q&A support  
✔ Simplified understanding  

</p>

</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # PERSONALIZED FLOW
    # =====================================================

    if personalized_clicked:

        st.markdown("---")

        st.success(
            """
✅ Great choice.

This personalized guidance is designed to help beginners gain practical investing clarity step-by-step.
"""
        )

        st.subheader("👑 What You Will Receive")

        st.write(
            """
• Beginner-focused investing understanding  
• Risk clarity explanation  
• Personalized investing observations  
• Simplified financial explanations  
• Beginner-friendly guidance approach  
"""
        )

        st.markdown("---")

        st.subheader("💳 Payment Process")

        st.write(
            """
1. Complete payment using the QR code below  
2. Fill the personalization form  
3. Receive beginner-focused investing clarity  
"""
        )

        # =================================================
        # QR IMAGE
        # =================================================

        try:

            st.image(
                "clarity_invest_qr.JPEG",
                width=260
            )

        except:

            st.warning(
                "QR image not uploaded yet."
            )

        st.markdown("")

        # =================================================
        # FORM BUTTON
        # =================================================

        st.link_button(

            "📝 Proceed to Personalized Guidance Form",

            "https://docs.google.com/forms/d/1NxGIVfxyViyLncwt299FWVOxrH5dv5tGjVYz-abg-EM/edit",

            use_container_width=True
        )

    # =====================================================
    # TRUST SECTION
    # =====================================================

    st.markdown("---")

    st.subheader("🤝 Beginner-Focused Philosophy")

    st.warning(
        """
Clarity Invest focuses on:
        
✅ investing understanding  
✅ financial awareness  
✅ beginner learning  
✅ risk understanding  

This platform does NOT promise:
        
❌ guaranteed returns  
❌ stock tips  
❌ unrealistic profits  
"""
    )

    # =====================================================
    # CONTACT SECTION
    # =====================================================

    st.markdown("---")

    st.subheader("📩 Connect With Clarity Invest")

    st.markdown(
        """
<div style='
padding:25px;
border-radius:20px;
background: rgba(17,24,39,0.95);
border:1px solid rgba(255,255,255,0.06);
'>

<p style='font-size:25px;'>

📸 Instagram:<br>
<a href='https://www.instagram.com/clarity_invest_insights' target='_blank'>
@clarity_invest_insights
</a>

<br><br>

💼 LinkedIn<br>

<a href='https://www.linkedin.com' target='_blank'>
LinkedIn Profile
</a>

<br><br>

🎯 Beginner-focused investing clarity platform

</p>

</div>
""",
        unsafe_allow_html=True
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