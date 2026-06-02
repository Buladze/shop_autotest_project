from .pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
    "password,expected_result", [
        ("secret_sauce", "success"),
        ("wrong_password", "error")
    ]
)
def test_guest_can_login(browser, password, expected_result):
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_button()
    login_page.login(password)
    if expected_result == "success":
        main_page = login_page.go_to_main_page()
        main_page.should_be_main_page()
        print(f"Успешный вход с паролем: {password}")
    else:
        error_message = login_page.get_error_message()
        assert error_message is not None, "Должно быть сообщение об ошибке"
        assert "Username and password do not match" in error_message, f"Неожиданное сообщение об ошибке: {error_message}"
        print(f"Ожидаемая ошибка с паролем: {password}")