import allure
from allure_commons.types import Severity
from selene import browser, by, have


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'k-brsky')
    allure.dynamic.feature('Таб Issues')
    allure.dynamic.story('Найти таб Issues')
    allure.dynamic.link('"https://github.com", name="Testing"')


def test_github_with_steps(params_for_browser):
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('k-brsky/qa_guru_8').press_enter()

    with allure.step('Переходим по ссылке на репозиторий'):
        browser.element(by.link_text('k-brsky/qa_guru_8')).click()

    with allure.step('Проверяем название кнопки Issues'):
        browser.element('#issues-tab').should(have.exact_text('Issues'))
