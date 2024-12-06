from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login()
        page = LoginPage(browser, browser.current_url)
        new_email = randomword(6) + "@fakemail.com"
        page.register_new_user(new_email, "9sdfasdaa")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.basket_should_not_contain_items()
    page.basket_should_be_empty()


@pytest.mark.skip
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.should_not_see_success_message()


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_see_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
def test_message_disappeared_after_adding_product(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.should_disappear_success_message()
