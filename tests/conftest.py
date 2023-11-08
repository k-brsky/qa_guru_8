import pytest
from selene import browser
from users.students import User
import datetime


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.driver.set_window_size(1980, 1080)
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()


@pytest.fixture(scope='module')
def create_user():
    return User(
        name='Poligraf',
        last_name='Sharikov',
        email='poligraf@sharikov.com',
        gender='Male',
        phone_number='1234567890',
        date_of_birth=datetime.date(1990, 5, 10),
        subject='Chemistry',
        hobby='Reading',
        photo='822806.jpg',
        current_addres='ulitsa Pushkina, dom Kolotushkina',
        state='Haryana',
        city='Karnal'
    )
