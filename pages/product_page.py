from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def enter_code(self):
        self.solve_quiz_and_get_code()

    def add_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, should not be'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message did not disappear, should be'
