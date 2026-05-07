import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.pages.shop_page import ShopPage


@pytest.fixture(scope="function")
def browser():
    # Создаем сервис для управления драйвером
    service = Service(ChromeDriverManager().install())

    # Создаем опции браузера (можно настроить дополнительные параметры)
    options = webdriver.ChromeOptions()

    # Создаем экземпляр драйвера с сервисом и опциями
    driver = webdriver.Chrome(service=service, options=options)

    # Возвращаем драйвер для использования в тестах
    yield driver

    # Завершаем работу драйвера после выполнения теста
    driver.quit()


@allure.title("Проверка итоговой суммы заказа")
@allure.description("Тест проверяет оформление "
                    "заказа и итоговую сумму товаров.")
@allure.feature("Корзина и оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_total_sum(browser):
    shop_page = ShopPage(browser)

    with allure.step("Открыть страницу авторизации"):
        shop_page.open_page_authorization()

    with allure.step("Ввести логин и пароль"):
        shop_page.input_login("standard_user")
        shop_page.input_password("secret_sauce")

    with allure.step("Нажать кнопку входа"):
        shop_page.press_button_login()

    with allure.step("Добавить товары в корзину"):
        shop_page.add_the_desired_items_to_the_cart()

    with allure.step("Перейти в корзину"):
        shop_page.go_in_cart()

    with allure.step("Начать оформление заказа (Checkout)"):
        shop_page.press_button_checkout()

    with allure.step("Ввести данные клиента"):
        shop_page.input_first_name("Вероника")
        shop_page.input_last_name("Бова")
        shop_page.input_postal_code("350000")

    with allure.step("Нажать Continue для завершения заказа"):
        shop_page.press_button_continue()

        # Проверка (Assertion)
    with allure.step("Получить итоговую сумму и проверить её значение"):
        itog_sum = shop_page.get_itog_sum()
        assert itog_sum == "$58.29", (f"Ошибка. Итоговая сумма не верна. "
                                      f"Ожидалось $58.29, получено {itog_sum}")
