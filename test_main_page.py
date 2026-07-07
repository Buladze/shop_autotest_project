from .pages.login_page import LoginPage
from .pages.data import LoginPageData, ErrorMessages
import pytest

BASE_URL = "https://www.saucedemo.com/"

# --- СЦЕНАРИЙ 1: ЛОГИН С РАЗНЫМИ ПАРОЛЯМИ ---
@pytest.mark.parametrize(
    "test_data", 
    LoginPageData.PASSWORDS,
    ids=[f"password_{data['password']}" for data in LoginPageData.PASSWORDS]
)
def test_guest_can_login(browser, test_data):
    
    login_page = LoginPage(browser, BASE_URL)
    login_page.open()
    login_page.should_be_login_button()
    
    password = test_data["password"]
    expected_result = test_data["expected"]
    
    login_page.login(password)
    
    if expected_result == "success":
        main_page = login_page.go_to_main_page()
        main_page.should_be_main_page()
        print(f"Успешный вход с паролем: {password}")
    else:
        error_message = login_page.get_error_message()
        assert error_message is not None, "Должно быть сообщение об ошибке"
        assert error_message == ErrorMessages.INVALID_CREDENTIALS, f"Неожиданное сообщение об ошибке: {error_message}"
        print(f"Ожидаемая ошибка с паролем: {password}")

# --- СЦЕНАРИЙ 2: РАБОТА С КОРЗИНОЙ ---
@pytest.mark.smoke
def test_guest_can_manage_cart(browser, valid_login):
    
    main_page = valid_login
    print("Успешный вход на главную страницу")
    
    main_page.add_to_cart()
    print("Товар добавлен в корзину")
    
    main_page.should_be_red_badge_of_added()
    print("Красный бейдж отображается корректно")
    
    main_page.click_to_cart_page()
    cart_page = main_page.go_to_cart_page()
    cart_page.should_be_cart_page()
    print("Переход на страницу корзины выполнен")

    cart_page.remove_from_cart()
    print("Товар удален из корзины")

    cart_page.should_not_be_cart_item_window()
    print("Корзина пуста после удаления")
    
    print("Сценарий управления корзиной успешно выполнен!")


# --- СЦЕНАРИЙ 3: СОРТИРОВКА ТОВАРОВ НА ГЛАВНОЙ СТРАНИЦЕ ---
@pytest.mark.regression
def test_guest_can_sort_items(browser, valid_login):

    main_page = valid_login
    
    sort_tests = [
        ("az", sorted, "по имени (A-Z)"),
        ("za", lambda x: sorted(x, reverse=True), "по имени (Z-A)"),
        ("lohi", sorted, "по цене (низкая-высокая)"),
        ("hilo", lambda x: sorted(x, reverse=True), "по цене (высокая-низкая)")
    ]
    
    for sort_type, sort_func, description in sort_tests:
        main_page.click_to_sort_button(sort_type)
        
        if "имени" in description:
            items = main_page.get_product_names()
        else:
            items = main_page.get_product_prices()
        
        assert items == sort_func(items), f"Товары не отсортированы {description}"
        print(f"Сортировка {description} работает корректно")
    
    print("Сценарий сортировки товаров успешно выполнен!")
