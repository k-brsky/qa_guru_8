from selene import browser, have, command
import os.path
from users.students import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register_user(self, user: User):
        browser.element('#firstName').click().type(user.name)
        browser.element('#lastName').click().type(user.last_name)
        browser.element('#userEmail').click().type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').click().type(user.phone_number)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()

        browser.element("#subjectsInput").type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobby)).click()

        browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(
            os.path.abspath(f'resources/{user.photo}'))

        browser.element('#currentAddress').type(user.current_addres)

        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()

        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()

        browser.element('#submit').perform(command.js.click)

    def assert_submitted_form(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.name} {user.last_name}',
                user.email,
                user.gender,
                user.phone_number,
                user.date_of_birth.strftime('%d %B,%Y'),
                user.subject,
                user.hobby,
                user.photo,
                user.current_addres,
                f'{user.state} {user.city}',
            )
        )
