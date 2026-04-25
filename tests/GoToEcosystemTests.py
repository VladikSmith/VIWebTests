import allure
from core.BaseTest import browser
from pages import LoginPage
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    Login_page = LoginPageHelper(browser)
    current_window_id = Login_page.get_windows_id(0)
    Login_page.click_vk_ecosystem()
    Login_page.click_more_button()
    new_window_id = Login_page.get_windows_id(1)
    Login_page.switch_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)
