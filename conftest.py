import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def _ensure_dirs():
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1400,900")
    driver = webdriver.Chrome(options=options)

    yield driver

    failed = getattr(request.node, "rep_call", None)
    if failed and failed.failed:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        name = f"screenshots/{request.node.name}_{ts}.png"
        try:
            driver.save_screenshot(name)
        except Exception:
            pass
    driver.quit()


def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames:
        if not hasattr(item, "rep_setup"):
            item.rep_setup = None
            item.rep_call = None
        if call.when == "setup":
            item.rep_setup = call
        elif call.when == "call":
            item.rep_call = call
