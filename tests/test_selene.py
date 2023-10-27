from selene import browser, have, by


def test_github(params_for_browser):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('k-brsky/qa_guru_8').press_enter()
    browser.element(by.link_text('k-brsky/qa_guru_8')).click()

    # THEN
    browser.element('#issues-tab').should(have.exact_text('Issues'))
