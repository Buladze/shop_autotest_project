from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    USERNAME_BOX = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_BOX = (By.CSS_SELECTOR, "[data-test='password']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

class MainPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory '])[1]")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")
    RED_BADGE_OF_ADDED = (By.CSS_SELECTOR, ".shopping_cart_badge")

class CartPageLocators():
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    CART_ITEM_WINDOW = (By.CSS_SELECTOR, ".cart_item")