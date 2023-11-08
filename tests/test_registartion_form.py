from qa_guru_8.pages.registration_page import RegistrationPage


def test_form(create_user):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register_user(create_user)

    # THEN

    registration_page.assert_submitted_form(create_user)
