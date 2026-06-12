from .base_page import BasePage
from .data import MainPageData, CartPageData
from .locators import MainPageLocators
from .cart_page import CartPage

class MainPage(BasePage): 
    def should_be_main_page(self):
        self.verify_url(MainPageData.URL_PAGE)

    def add_to_cart(self):
        button = self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_red_badge_of_added(self):
        assert self.is_element_present(*MainPageLocators.RED_BADGE_OF_ADDED), "Should be red badge of added product"

    def click_to_cart_page(self):
        button = self.browser.find_element(*MainPageLocators.CART_BUTTON)
        button.click()

    def go_to_cart_page(self):
        return CartPage(browser=self.browser, url=CartPageData.URL_PAGE)
        