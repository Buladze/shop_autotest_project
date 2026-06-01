from selenium.common.exceptions import NoSuchElementException

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

    def get_current_url(self):
        return self.browser.current_url

    def verify_url(self, expected_url):
        current = self.get_current_url()
        assert current == expected_url, f"URL wrong: expected {expected_url}, got {current}"