from .base_page import BasePage
from .locators import LoginPageLocators
from .data import LoginPageData

class LoginPage(BasePage): 
    def login(self):
        username_box = self.browser.find_element(*LoginPageLocators.USERNAME_BOX)
        username_box.send_keys(*LoginPageData.USERNAME)
        password_box = self.browser.find_element(*LoginPageLocators.PASSWORD_BOX)
        password_box.send_keys(*LoginPageData.PASSWORD)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()
        
        
    
    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Should be login button"