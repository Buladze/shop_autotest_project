from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    USERNAME_BOX = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_BOX = (By.CSS_SELECTOR, "[data-test='password']")