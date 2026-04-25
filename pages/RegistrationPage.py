from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@class="vkuiFormField__content"]')
    COUNTRY_LIST = (By.XPATH, '//div[@class="PhoneInput-module_phoneInput_numberIconInner__saRYB"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="CountryList-module_countryList__listItemCode__LzHon"]')
    SUBMIT_BUTTON = (By.XPATH,
                     '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modePrimary vkuiButton__appearanceAccent vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    ABOUT_VK = (By.XPATH,
                '//a[contains(@href, "https://id.vk.com/promo")]')


class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.ABOUT_VK)

    def select_random_country(self):
        with allure.step('Рандомно выбираем страну из списка'):
            random_number = random.randint(0, 212)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
            country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
            country_code = country_items[random_number].get_attribute('text')
            country_items[random_number].click()
            return country_code

    def get_phone_field_value(self):
        with allure.step('Получение кода выбранной страны'):
            return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
