from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    ENTRY_BUTTON = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH,
                                 '//*[@class="vkuiInternalTappable vkuiIconButton__host vkuiIconButton__sizeYNone vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_BUTTON = (By.XPATH,
                    '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modePrimary vkuiButton__appearanceAccent vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    ENTRY_BY_QR_CODE_BUTTON = (By.XPATH,
                               '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeOutline vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    CANT_LOGIN = (By.XPATH,
                  '//*[@class="vkuiInternalTappable vkuiLink__host vkuiLink__withUnderline vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    REGISTRATION_BUTTON = (By.XPATH,
                           '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_BY_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BY_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BY_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH,
                  '//*[@class="LoginForm-module__error___1xmAD vkuiCaption__sizeYNone vkuiCaption__level1 vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')
    RESTORE_BUTTON = (By.XPATH,
                      '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modePrimary vkuiButton__appearanceAccent vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    GO_BACK_BUTTON = (By.XPATH,
                      '//div[@class="vkuiButtonGroup__host vkuiButtonGroup__modeVertical vkuiButtonGroup__gapM vkuiButtonGroup__stretched vkuiButtonGroup__alignLeft vkuiRootComponent__host"]/button[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.ENTRY_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.ENTRY_BY_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.CANT_LOGIN)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_VK)
        self.find_element(LoginPageLocators.LOGIN_BY_MAIL)
        self.find_element(LoginPageLocators.LOGIN_BY_YANDEX)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логина')
    def fill_login_field(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароля')
    def fill_password_field(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()
