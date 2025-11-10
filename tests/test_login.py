import pytest

@pytest.mark.xfail(reason="demo screenshot check", strict=False)
def test_fail_screenshot(driver):
    driver.get("https://example.com")
    assert False
