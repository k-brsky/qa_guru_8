import pytest
from selene import browser, be, have

@pytest.fixture(scope='function')
def browser_open():
    browser.open('https://www.google.com')
    browser.driver.set_window_size(1980, 1080)

    yield

    browser.close()

def test_google_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests'))

def test_google_not_found(browser_open):
    browser.element('[name="q"]').should(be.blank).type('енаппгпшграпне').press_enter()
    browser.element('[id="center_col"]').should(have.text('ничего не найдено'))