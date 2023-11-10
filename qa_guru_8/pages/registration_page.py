from selene import browser, have, command
from qa_guru_8.paths import path_to_image


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').click().type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').click().type(value)

    def fill_email(self, value):
        browser.element('#userEmail').click().type(value)

    def choose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').click().type(value)

    def fill_birthday(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def choose_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    def upload_image(self, file_name):
        browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(path_to_image.path(file_name))

    def fill_current_adress(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def choose_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    @property
    def assert_submitted_form(self):
        return browser.element('.table').all('td').even
