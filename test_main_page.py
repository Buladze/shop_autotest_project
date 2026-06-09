from .pages.login_page import LoginPage
from .pages.data import LoginPageData, ErrorMessages
import pytest

@pytest.mark.parametrize(
    "test_data", LoginPageData.PASSWORDS
)
def test_guest_can_login(browser, test_data):
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.should_be_login_button()
    
    password = test_data["password"]
    expected_result = test_data["expected"]
    
    login_page.login(password)
    
    if expected_result == "success":
        main_page = login_page.go_to_main_page()
        main_page.should_be_main_page()
        print(f"Успешный вход с паролем: {password}")
        main_page.add_to_cart()
        main_page.should_be_red_badge_of_added()
    
    else:
        error_message = login_page.get_error_message()
        assert error_message is not None, "Должно быть сообщение об ошибке"
        assert error_message == ErrorMessages.INVALID_CREDENTIALS, f"Неожиданное сообщение об ошибке: {error_message}"
        print(f"Ожидаемая ошибка с паролем: {password}")

    