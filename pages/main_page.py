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

    def click_to_sort_button(self, sort_type="az"):
        sort_dropdown = self.browser.find_element(*MainPageLocators.SORT_DROPDOWN)
        sort_dropdown.click()
        
        sort_options = {
            "az": MainPageLocators.SORT_A_TO_Z,
            "za": MainPageLocators.SORT_Z_TO_A,
            "lohi": MainPageLocators.SORT_LOW_TO_HIGH_PRICE,
            "hilo": MainPageLocators.SORT_HIGH_TO_LOW_PRICE
        }
        
        option = self.browser.find_element(*sort_options[sort_type])
        option.click()
    
    def get_product_names(self):
        name_elements = self.browser.find_elements(*MainPageLocators.PRODUCT_NAMES)
        return [element.text for element in name_elements]
    
    def get_product_prices(self):
        price_elements = self.browser.find_elements(*MainPageLocators.PRODUCT_PRICES)
        return [float(element.text.replace('$', '')) for element in price_elements]
