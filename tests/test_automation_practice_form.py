import os.path
from selene import browser, command, have


def test_form():
    # сам тест

    browser.open('/automation-practice-form')

    browser.element('#firstName').click().type('Poligraf')
    browser.element('#lastName').click().type('Sharikov')
    browser.element('#userEmail').click().type('poligraf@sharikov.com')
    browser.element("//label[@for='gender-radio-1']").click()
    browser.element('#userNumber').click().type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('//select/option[@value="4"]').click()
    browser.element('.react-datepicker__year-select').click().element('//select/option[@value="1990"]').click()
    browser.element('//div[@class="react-datepicker__day react-datepicker__day--010"]').click()

    browser.element("#subjectsInput").type("C")
    browser.element("//*[contains(text(), 'Chemistry')]").click()

    browser.element("//label[@for='hobbies-checkbox-2']").click()
    browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(os.path.abspath("822806.jpg"))

    browser.element('#currentAddress').type('ulitsa Pushkina, dom Kolotushkina')

    browser.element("//*[contains(text(), 'Select State')]").perform(command.js.scroll_into_view).click()
    browser.element("//*[contains(text(), 'Haryana')]").click()

    browser.element("//*[contains(text(), 'Select City')]").click()
    browser.element("//*[contains(text(), 'Karnal')]").perform(command.js.scroll_into_view).click()

    browser.element('#submit').execute_script("element.click()")

    # проверочки

    browser.element("//tbody/tr[1]").should(have.text("Poligraf Sharikov"))
    browser.element("//tbody/tr[2]").should(have.text("poligraf@sharikov.com"))
    browser.element("//tbody/tr[3]").should(have.text("Male"))
    browser.element("//tbody/tr[4]").should(have.text("1234567890"))
    browser.element("//tbody/tr[5]").should(have.text("10 May,1990"))
    browser.element("//tbody/tr[6]").should(have.text("Chemistry"))
    browser.element("//tbody/tr[7]").should(have.text("Reading"))
    browser.element("//tbody/tr[8]").should(have.text("822806.jpg"))
    browser.element("//tbody/tr[9]").should(have.text("ulitsa Pushkina, dom Kolotushkina"))
    browser.element("//tbody/tr[10]").should(have.text("Haryana Karnal"))
