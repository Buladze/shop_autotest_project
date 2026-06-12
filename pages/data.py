from selenium.webdriver.common.by import By

class LoginPageData():
    USERNAME = "standard_user"
    PASSWORDS = [
       {"password": "secret_sauce", "expected": "success"},
       {"password": "wrong_password", "expected": "error"}
]

class MainPageData():
    URL_PAGE = "https://www.saucedemo.com/inventory.html"

class CartPageData():
    URL_PAGE = "https://www.saucedemo.com/cart.html"

class ErrorMessages():
    INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"