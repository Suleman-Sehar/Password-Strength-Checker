import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!👋
 use this simple tool to evaluate the strength of your passwords and ensure your online security.
    we will give you a helpfull tips to create a **Strong Password**""")

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit.")
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character.(!@#$%&*)")
    if score == 4:
        feedback.append("✅ Your password is strong!")
    elif score == 3:
        feedback.append("⚠️ Your password is medium strength.")
    else:
        feedback.append("❌ Your password is weak.")
    
    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.markdown(tip)
else:
    st.info("Please enter a password to check its strength.")