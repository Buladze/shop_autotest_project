from .pages.login_page import LoginPage
import pytest


def test_guest_can_login(browser, request):
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_button()
    login_page.login()
    main_page = login_page.go_to_main_page()
    main_page.should_be_main_page()