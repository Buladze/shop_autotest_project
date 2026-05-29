# from .pages.main_page import MainPage
# import pytest
from selenium.webdriver.common.by import By


def test_guest_can_go_to_start_page(browser, request):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#user-name")
    login_link.click()