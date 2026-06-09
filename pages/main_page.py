from .base_page import BasePage
from .data import MainPageData
from .locators import MainPageLocators

class MainPage(BasePage): 
    def should_be_main_page(self):
        self.verify_url(MainPageData.URL_PAGE)

    def add_to_cart(self):
        button = self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_red_badge_of_added(self):
        assert self.is_element_present(*MainPageLocators.RED_BADGE_OF_ADDED), "Should be red badge of added product"
        