from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def enter_code(self):
        self.solve_quiz_and_get_code()
    def add_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()