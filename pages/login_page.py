from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage): 
    # def go_to_search(self):
        # login_link = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        # login_link.click()
    
    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Should be login button"