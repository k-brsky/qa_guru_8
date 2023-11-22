import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_8.utils import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1%1234@selenoid:autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()