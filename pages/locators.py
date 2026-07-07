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
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_A_TO_Z = (By.XPATH, "//option[@value='az']")
    SORT_Z_TO_A = (By.XPATH, "//option[@value='za']")
    SORT_LOW_TO_HIGH_PRICE = (By.XPATH, "//option[@value='lohi']")
    SORT_HIGH_TO_LOW_PRICE = (By.XPATH, "//option[@value='hilo']")

class CartPageLocators():
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    CART_ITEM_WINDOW = (By.CSS_SELECTOR, ".cart_item")