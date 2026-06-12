from .base_page import BasePage
from .data import CartPageData
from .locators import CartPageLocators

class CartPage(BasePage): 
    def should_be_cart_page(self):
        self.verify_url(CartPageData.URL_PAGE)

    def remove_from_cart(self):
        button = self.browser.find_element(*CartPageLocators.REMOVE_BUTTON)
        button.click()
        
    def should_not_be_cart_item_window(self):
        assert self.is_element_not_present(*CartPageLocators.CART_ITEM_WINDOW), "Cart item window should not be present after removal"