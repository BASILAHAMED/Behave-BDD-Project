# Behave-BDD-Project

**Behave + Selenium + Allure + SauceDemo login test**

# 🧪 SauceDemo Login Automation with Behave, Selenium & Allure

This project demonstrates automated login testing for the [SauceDemo](https://www.saucedemo.com/) website using **Python Behave (BDD)**, **Selenium WebDriver**, and **Allure Reports**.

---

## 📂 Project Structure

```

behave-saucedemo-login/
├── features/
│   ├── login.feature
│   ├── steps/
│   │   └── login_steps.py
│   └── environment.py
├── pages/
│   └── login_page.py
├── drivers/
│   └── chromedriver (optional)
├── reports/
│   └── allure-results/
│   └── allure-report/
├── requirements.txt
├── behave.ini
└── README.md

````

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Behave-BDD-Project.git
cd Behave-BDD-Project
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests with Behave

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

---

## 📊 Generating Allure HTML Report

### Install Allure CLI (one-time setup)

#### Option 1: Using Scoop (recommended for Windows)

```bash
scoop install allure
```

---

### Generate and View Report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

## ✅ Scenarios Covered

* ✅ Successful login with valid credentials
* ❌ Unsuccessful login with invalid credentials

---

## 📌 Tech Stack

* 🐍 Python 3
* 🧪 Behave (BDD framework)
* 🌐 Selenium WebDriver
* 📊 Allure Reporting
* 🧱 Page Object Model (POM) design

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 📄 License

MIT License

---
