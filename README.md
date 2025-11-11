[![codecov](https://codecov.io/gh/fanoctism/selenium-login-tests/branch/main/graph/badge.svg)](https://codecov.io/gh/fanoctism/selenium-login-tests)
[![Tests](https://github.com/fanoctism/selenium-login-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/fanoctism/selenium-login-tests/actions/workflows/tests.yml)

# Selenium Login Tests

![Python](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-brightgreen)

Automated web UI tests built with **Selenium**, **Pytest**, and **GitHub Actions**.

## Features
- End to end login validation tests
- HTML reports with pytest html
- GitHub Actions CI integration
- WebDriver auto download via webdriver manager
- Pre commit hooks Black Flake8 isort

## Setup
```bash
git clone https://github.com/fanoctism/selenium-login-tests.git
cd selenium-login-tests

python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt

## Run tests locally
- pytest -v
- pytest -v --html=report.html --self-contained-html

After running tests

report.html contains the HTML report
screenshots are saved on failure if any

## CI
Workflow file: .github/workflows/tests.yml
Triggers: push to main and pull_request into main

Artifacts uploaded
pytest-report which contains report.html

screenshots if failures occurred

## Code style
pre-commit install
pre-commit run --all-files
