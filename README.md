![Tests](https://github.com/fanoctism/selenium-login-tests/actions/workflows/pytest.yml/badge.svg)

# Selenium Login Tests

![Python](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-brightgreen)

Automated web UI tests built with **Selenium**, **Pytest**, and **GitHub Actions**.

---

## 🚀 Features

- End-to-end login validation tests  
- HTML test reports (`pytest-html`)  
- GitHub Actions CI integration  
- Auto-download of WebDriver via `webdriver-manager`  
- Pre-commit hooks for linting (Black, Flake8, isort)  

---

## 🧪 Run tests locally

```bash
# activate virtual environment (Windows)
.\.venv\Scripts\activate

# run tests with HTML report
pytest -v --html=reports/report.html --self-contained-html
