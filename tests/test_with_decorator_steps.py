import allure
from allure_commons.types import Severity
from selene import browser, by, have


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'k-brsky')
@allure.feature('Таб Issues')
@allure.story('Найти таб Issues')
@allure.link('"https://github.com", name="Testing"')
def test_github_with_decorator_steps(params_for_browser):
    open_main_page()
    search_repository('k-brsky/qa_guru_8')
    go_to_repository('k-brsky/qa_guru_8')
    check_issues()


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repository_name}')
def search_repository(repository_name):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repository_name).press_enter()


@allure.step('Переходим по ссылке на репозиторий {repository_name}')
def go_to_repository(repository_name):
    browser.element(by.link_text(repository_name)).click()


@allure.step('Проверяем кнопку Issues')
def check_issues():
    browser.element('#issues-tab').should(have.exact_text('Issues'))
