# Selenium Login & Sorting Tests

Simple, clean UI tests with Python, Selenium, and PyTest.  
Covers two flows:
- Login on saucedemo.com
- Sorting by name (A - Z) on an OpenCart category page

## Tech
- Python 3.12
- Selenium 4
- PyTest
- WebDriver Manager

## Project structure
- pages/ - Page Objects
- tests/ - test suites
- utils/ - helpers
- requirements.txt

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt

## Run
```bash
pytest -q
# headless (no browser window)
set HEADLESS=1 && pytest -q

## Tests
- `tests/test_login.py` - valid login on 'saucedemo.com'  
- `tests/test_sorting.py` - 'Name (A - Z)' sorting on OpenCart

## Notes
- Use CSS selectors where possible, avoid sleeps, prefer explicit waits.  
- Fixed window size for stability: 1280x900.  
- Selenium Manager handles driver automatically.

## Next steps
- Add negative login test (wrong password).  
- Add logout test.  
- Add GitHub Actions workflow to run tests on push.

