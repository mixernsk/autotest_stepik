from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@class='content']//p[contains(text(), 'empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//a[contains(@href,"basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    LOGIN_URL = 'login'
    REG_EMAIL = (By.ID, 'id_registration-email')
    REG_PASSWORD1 = (By.ID, 'id_registration-password1')
    REG_PASSWORD2 = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.XPATH, '//button[contains(@name, "registration")]')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']//div[@class='alertinner ']/strong")