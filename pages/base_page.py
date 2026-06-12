from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, how, what):
        try:
            WebDriverWait(self.browser, timeout=2).until(
                EC.presence_of_element_located((how, what))
            )
            return False
        except TimeoutException:
            return True
            
    def get_current_url(self):
        return self.browser.current_url

    def verify_url(self, expected_url):
        current = self.get_current_url()
        assert current == expected_url, f"URL wrong: expected {expected_url}, got {current}"