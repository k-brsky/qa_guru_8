import pytest
from selene import browser


@pytest.fixture(scope='function')
def params_for_browser():
    browser.driver.set_window_size(1440, 960)
