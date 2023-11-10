from selene import have
from qa_guru_8.pages.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN

    registration_page.fill_first_name('Poligraf')
    registration_page.fill_last_name('Sharikov')
    registration_page.fill_email('poligraf@sharikov.com')
    registration_page.choose_gender('Male')
    registration_page.fill_number('1234567890')
    registration_page.fill_birthday(10, 'May', 1990)
    registration_page.fill_subject('Chemistry')
    registration_page.choose_hobby('Reading')
    registration_page.upload_image('photo.jpg')
    registration_page.fill_current_adress('ulitsa Pushkina, dom Kolotushkina')
    registration_page.choose_state('Haryana')
    registration_page.choose_city('Karnal')
    registration_page.submit()

    # THEN

    registration_page.assert_submitted_form.should(
        have.exact_texts(
            'Poligraf Sharikov',
            'poligraf@sharikov.com',
            'Male',
            '1234567890',
            '10 May,1990',
            'Chemistry',
            'Reading',
            'photo.jpg',
            'ulitsa Pushkina, dom Kolotushkina',
            'Haryana Karnal',
        )
    )
