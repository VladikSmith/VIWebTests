from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure
import time

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Login required'
EMPTY_PASSWORD_ERROR = 'Password required'
LOGIN_TEXT = 'email'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    time.sleep(5)
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


@allure.title('Проверка ошибки при авторизации без пароля')
def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.fill_login_field(LOGIN_TEXT)
    LoginPage.click_login()
    time.sleep(5)
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR
