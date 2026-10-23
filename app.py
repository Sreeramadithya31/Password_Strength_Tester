import streamlit as st
import re


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Password Strength Tester",
    page_icon="🔐",
    layout="centered"
)


# -----------------------------
# Password Analysis Function
# -----------------------------

def check_password(password):

    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback


# -----------------------------
# User Interface
# -----------------------------

st.title("🔐 Password Strength Tester")

st.write(
    "Check the strength of a password using basic cybersecurity "
    "security requirements."
)

st.divider()

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter password here..."
)


# -----------------------------
# Analyze Password
# -----------------------------

if password:

    score, strength, feedback = check_password(password)

    st.subheader("Password Analysis")

    # Strength display
    if strength == "Strong":
        st.success(f"🟢 Strength: {strength}")

    elif strength == "Medium":
        st.warning(f"🟠 Strength: {strength}")

    else:
        st.error(f"🔴 Strength: {strength}")

    # Score
    st.write(f"**Security Score:** {score}/5")

    # Progress bar
    st.progress(score / 5)

    st.subheader("Security Checks")

    # Length
    if len(password) >= 8:
        st.write("✅ At least 8 characters")
    else:
        st.write("❌ At least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        st.write("✅ Contains uppercase letter")
    else:
        st.write("❌ Contains uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        st.write("✅ Contains lowercase letter")
    else:
        st.write("❌ Contains lowercase letter")

    # Number
    if re.search(r"[0-9]", password):
        st.write("✅ Contains number")
    else:
        st.write("❌ Contains number")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        st.write("✅ Contains special character")
    else:
        st.write("❌ Contains special character")

    # Suggestions
    if feedback:

        st.subheader("💡 Suggestions")

        for item in feedback:
            st.write("• " + item)

    else:

        st.success(
            "Your password satisfies all the basic security requirements!"
        )


# -----------------------------
# Project Information
# -----------------------------

st.divider()

st.subheader("About the Project")

st.write(
    """
    This Password Strength Tester is a cybersecurity application
    that evaluates passwords using common security rules.

    It checks password length, uppercase letters, lowercase letters,
    numbers, and special characters.
    """
)