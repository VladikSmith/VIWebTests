from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTRY_BUTTON = (By.XPATH, '//*[@data-l="t,login_tab"]]')
    QR_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH,
                                 '//*[@class="vkuiInternalTappable vkuiIconButton__host vkuiIconButton__sizeYNone vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    ENTRY_BY_QR_CODE_BUTTON = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    CANT_LOGIN = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH,
                           '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_BY_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BY_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BY_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelper(BasePage):
    pass
