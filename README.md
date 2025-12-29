# 🚀 Mastering Web Automation with Selenium (Python)

A **complete, hands-on Selenium 4.x automation repository** built using **Python + PyTest**, designed for real-world web automation, framework building, and interview readiness.

This repository is derived from **structured Selenium training notes** and focuses on **practical execution**, not just theory.

---

## 📌 What This Repository Covers

This project walks you through **end-to-end Selenium automation**, starting from basics and progressing to advanced, production-level topics.

You will learn and implement:

* Selenium 4.x architecture (W3C Protocol)
* Python + Selenium setup (local, grid, Docker, cloud)
* Locators (XPath, CSS, Relative Locators)
* Wait strategies (Implicit, Explicit, Fluent)
* Actions, Alerts, Windows, iFrames
* Web Tables, File Uploads, SVG & Shadow DOM
* Page Object Model (POM & Page Factory)
* Data-driven testing using Excel
* Parallel execution with PyTest
* Reporting with Allure & HTML reports
* CI execution using Jenkins
* Grid execution (Local, Docker, AWS)

---

## 🧱 Repository Structure

```bash
selenium-python-automation/
│
├── README.md
│
├── requirements.txt
│
├── pytest.ini
│
├── .env
│
├── drivers/
│   ├── chromedriver
│   ├── geckodriver
│
├── tests/
│   ├── basic/
│   │   ├── test_navigation.py
│   │   ├── test_locators.py
│   │
│   ├── waits/
│   │   ├── test_implicit_wait.py
│   │   ├── test_explicit_wait.py
│   │
│   ├── actions/
│   │   ├── test_keyboard_mouse_actions.py
│   │
│   ├── windows_iframes/
│   │   ├── test_windows.py
│   │   ├── test_iframe.py
│   │
│   ├── alerts/
│   │   ├── test_js_alerts.py
│   │
│   ├── webtables/
│   │   ├── test_static_table.py
│   │   ├── test_dynamic_table.py
│   │
│   ├── svg_shadowdom/
│   │   ├── test_svg_elements.py
│   │
│   ├── datadriven/
│   │   ├── test_login_excel.py
│   │
│   └── pom/
│       ├── pages/
│       │   ├── login_page.py
│       │   └── dashboard_page.py
│       ├── tests/
│       │   └── test_login_pom.py
│
├── testdata/
│   ├── testdata.xlsx
│
├── reports/
│   ├── allure-results/
│   ├── html-report/
│
├── docker/
│   ├── docker-compose.yml
│
└── ci/
    ├── jenkinsfile
```

---

## ⚙️ Tech Stack

* **Language:** Python 3.9+
* **Automation:** Selenium 4.x
* **Test Framework:** PyTest
* **Reporting:** Allure, PyTest HTML
* **Data Driven:** openpyxl (Excel)
* **Parallel Execution:** pytest-xdist
* **CI/CD:** Jenkins
* **Grid:** Selenium Grid, Docker, AWS
* **OS:** Windows / macOS / Linux

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/selenium-python-automation.git
cd selenium-python-automation
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run Tests

### Run All Tests

```bash
pytest -v
```

### Run Specific Folder

```bash
pytest tests/waits -v
```

### Run in Parallel

```bash
pytest -n 4
```

---

## 📊 Reporting

### Allure Report

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### HTML Report

```bash
pytest --html=reports/html-report/report.html
```

---

## 🌐 Selenium Grid Execution

### Local Grid (Standalone)

```bash
java -jar selenium-server.jar standalone
```

### Docker Grid

```bash
docker-compose up -d
```

### Cloud Execution

* BrowserStack
* AWS + Jenkins
* Selenoid

---

## 🧠 Design Principles Used

* Page Object Model (POM)
* Clean separation of tests and pages
* Reusable locators & utilities
* Scalable folder structure
* CI-ready automation

---

## 📚 Learning Outcomes

After completing this repository, you will be able to:

* Build **industry-grade Selenium frameworks**
* Handle **real-world UI automation problems**
* Crack **SDET / Automation interviews**
* Execute tests on **Grid, Docker & Cloud**
* Integrate automation into **CI/CD pipelines**

---

## 👤 Author

**Abhishek Sawlikar**
www.linkedin.com/in/abhishek-sawlikar

---

## ⭐ Support

If this repository helps you:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Learn & Build
* 🚀 Share with fellow QAs

---
