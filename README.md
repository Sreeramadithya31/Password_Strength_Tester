# 🔐 Password Strength Tester | Python & Streamlit

🚀 **A simple, interactive cybersecurity application that analyzes password strength and helps users create stronger, more secure passwords!**

The **Password Strength Tester** is a Python-based web application built using **Streamlit** that evaluates password strength based on five essential security criteria. It provides instant feedback, a security score, visual strength indicators, and personalized suggestions to help users improve their passwords.

This project demonstrates fundamental cybersecurity concepts, Python programming, regular expressions, and interactive web application development.

---

## ✨ Features

🔍 **Real-Time Password Analysis**  
Analyze a password instantly and receive feedback based on predefined security requirements.

📏 **Password Length Validation**  
Checks whether the password contains at least 8 characters.

🔠 **Uppercase Letter Detection**  
Verifies the presence of at least one uppercase letter (A–Z).

🔡 **Lowercase Letter Detection**  
Checks for at least one lowercase letter (a–z).

🔢 **Number Detection**  
Verifies whether the password contains at least one numeric digit (0–9).

🔣 **Special Character Detection**  
Checks for special characters such as `@`, `#`, `$`, `%`, and `!`.

📊 **Security Score**  
Displays a score out of 5 based on the number of criteria satisfied.

💪 **Password Strength Classification**  
Classifies passwords into three categories:
- 🔴 **Weak:** 0–2 criteria satisfied.
- 🟠 **Medium:** 3–4 criteria satisfied.
- 🟢 **Strong:** All 5 criteria satisfied.

💡 **Personalized Improvement Suggestions**  
Provides actionable feedback for missing security requirements.

📈 **Visual Progress Indicator**  
Displays a progress bar representing the password security score.

🖥️ **Interactive Web Interface**  
Provides a clean, user-friendly interface powered by Streamlit, with a masked password input field.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Interactive web interface |
| 🔎 Regular Expressions (`re`) | Password pattern validation |
| 📊 Streamlit Progress Bar | Visual security score |
| 🔐 Cybersecurity Concepts | Basic password security assessment |

---

## ⚙️ How It Works

The application evaluates the entered password against five conditions:

1. ✅ Password length is at least 8 characters.
2. ✅ Contains at least one uppercase letter.
3. ✅ Contains at least one lowercase letter.
4. ✅ Contains at least one number.
5. ✅ Contains at least one special character.

Each satisfied condition contributes one point to the total score.

The application then determines the strength category and displays the checks that passed or failed. If any conditions are not met, it provides suggestions to improve the password.

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/password_strength_tester.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd password_strength_tester
```

### 3️⃣ Install the Required Dependency

```bash
pip install streamlit
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

🌐 Streamlit will open the application in your browser. If it does not open automatically, visit:

`http://localhost:8501`

**Note:** Ensure your Python file is named `app.py`. If you use another filename, replace `app.py` in the command with your actual filename.

---

## 📂 Project Structure

```text
password_strength_tester/
│
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
```

---

## 🎯 Project Objectives

- 🔐 Understand basic password security requirements.
- 🐍 Apply Python programming concepts to a practical application.
- 🔎 Use regular expressions to identify password patterns.
- 🎈 Develop an interactive web application using Streamlit.
- 💡 Help users identify missing password complexity requirements.
- 🛡️ Promote awareness of stronger password practices.

---

## 🎓 Learning Outcomes

Through this project, I explored:

- Python functions and conditional statements.
- Regular expressions for text validation.
- Password strength scoring and classification.
- Interactive UI development with Streamlit.
- Real-time feedback and input validation.
- Fundamental cybersecurity and password hygiene concepts.

---

## 🔮 Future Enhancements

🚀 The project can be extended with the following features:

- 📏 Support for configurable password policies.
- ⏳ Estimated password-cracking time using an appropriate entropy model.
- 🚫 Detection of common and easily guessed passwords.
- 🛡️ Checks against known compromised passwords using a privacy-preserving approach.
- 📊 More detailed password entropy analysis.
- 📱 Improved responsive design and accessibility.
- 🔑 Secure password generator functionality.
- 🌐 Deployment as an online web application.

---

## 🔒 Security Note

This project is designed for **educational and basic password-strength assessment purposes**. The current implementation checks password length and character categories; it does not measure true password entropy, detect breached passwords, or guarantee resistance to password attacks.

Avoid entering your real or sensitive passwords into demonstration applications unless you trust how the application handles them.

---

## 👨‍💻 Author

**Ganti Sreeramaditya**

🎓 B.Tech – Computer Science and Engineering (Data Science)  
💻 Interests: Python, Data Science, AI/ML, Web Development, and Cybersecurity.

🌟 If you find this project useful, consider giving the repository a star!

⭐ **Star the repository | 🍴 Fork the project | 🤝 Contribute**

---

### 🏷️ Topics

`Python` `Streamlit` `Cybersecurity` `Password-Strength-Tester` `Password-Security` `Regular-Expressions` `Web-Application` `Python-Project` `Information-Security`
