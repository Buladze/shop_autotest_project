from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    USERNAME_BOX = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_BOX = (By.CSS_SELECTOR, "[data-test='password']")

class MainPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory '])[1]")
