from .base_page import BasePage
from .locators import LoginPageLocators
from .data import LoginPageData, MainPageData
from .main_page import MainPage

class LoginPage(BasePage): 
    def login(self, password):
        username_box = self.browser.find_element(*LoginPageLocators.USERNAME_BOX)
        username_box.send_keys(LoginPageData.USERNAME)
        password_box = self.browser.find_element(*LoginPageLocators.PASSWORD_BOX)
        password_box.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()
        
    
    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Should be login button"

    def go_to_main_page(self):
        return MainPage(browser=self.browser, url=MainPageData.URL_PAGE) 

    def get_error_message(self):
        error_locator = (LoginPageLocators.ERROR_MESSAGE)
        if self.is_element_present(*error_locator):
            return self.browser.find_element(*error_locator).text
        return None