🧪 Playwright Automation Framework (Python + Pytest)
📌 Overview

This is a production-ready automation framework built using:

Playwright (UI automation)
pytest (test runner)
Page Object Model (POM)
Layered architecture (tests → pages → core)

👉 Focus: Scalability, Maintainability, Reusability, CI/CD ready

🏗️ Project Structure (Industry Standard)
automation_framework/
│
├── tests/                      # WHAT to test (business scenarios)
│   └── test_login.py
│
├── pages/                      # Page Objects (business actions)
│   └── login_page.py
│
├── core/                       # HOW actions are executed (framework layer)
│   ├── base_page.py
│   ├── logger.py
│   └── playwright_manager.py   # (optional advanced control)
│
├── locators/                   # WHERE elements are
│   └── login_locator.py
│
├── utils/                      # Common utilities
│   ├── data_reader.py
│   └── helpers.py
│
├── config/                     # Environment/configuration
│   └── config.py
│
├── test_data/                  # Test data (JSON, CSV)
│   └── login_data.json
│
├── reports/                    # Test reports (Allure/HTML)
│
├── conftest.py                 # Fixtures (setup/teardown)
├── pytest.ini                  # Pytest configuration
├── requirements.txt
└── README.md
🔥 Architecture Flow (VERY IMPORTANT)
tests → pages → core → Playwright → Browser
Layer	Responsibility
tests	Business validation
pages	User actions
core	Reusable logic
Playwright	Execution engine
⚙️ Setup Instructions
1. Install dependencies
pip install -r requirements.txt
2. Install Playwright browsers
playwright install
▶️ Run Tests
pytest -v
Run with markers
pytest -m smoke