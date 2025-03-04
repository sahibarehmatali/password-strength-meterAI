import re
import random
import string
import streamlit as st  # GUI ke liye

#  Function to analyze password strength
def check_password_strength(password):
    score = 0
    feedback = []

    #  Blacklisted Common Passwords
    common_passwords = {"password123", "12345678", "qwerty", "abc123", "letmein"}
    if password in common_passwords:
        return 1, " This password is too common. Choose a more secure one."

    #  Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    #  Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" Include both uppercase and lowercase letters.")

    #  Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")

    #  Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" Include at least one special character (!@#$%^&*).")

    #  Pattern Analysis (Avoid repeated characters)
    if not re.search(r"(.)\1{2,}", password):  # No 3 same characters in a row
        score += 1
    else:
        feedback.append(" Avoid using the same character 3 times in a row.")

    #  Strength Rating & Feedback
    if score >= 5:
        return 5, " Strong Password! Your password meets all security requirements."
    elif score >= 3:
        return 3, " Moderate Password - Consider adding more security features."
    else:
        return 1, " Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback)

#  Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))

    # Ensure at least one character from each category
    while not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password)):
        password = ''.join(random.choice(characters) for _ in range(12))

    return password

#  Streamlit UI
def main():
    st.title(" Password Strength Meter")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, message = check_password_strength(password)
        st.write(message)
    
    if st.button("Generate Strong Password"):
        st.write(" Suggested Password:", generate_strong_password())

if __name__ == "__main__":
    main()
