from .pages.login_page import LoginPage
import pytest


def test_guest_can_go_to_start_page(browser, request):
    link = "https://www.saucedemo.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_button()
