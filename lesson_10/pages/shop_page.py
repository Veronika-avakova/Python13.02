from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """
    Класс-страница для взаимодействия с интернет-магазином SauceDemo.
    Объединяет логику авторизации, работы с корзиной и оформления заказа.
    """

    def __init__(self, browser):
        """
        Инициализация страницы.

        :param browser: Экземпляр WebDriver (браузера).
        """
        self._browser = browser
        self._browser.maximize_window()

    def open_page_authorization(self):
        """
        Открывает страницу авторизации магазина.

        :return: None
        """
        self._browser.get("https://www.saucedemo.com/")
        WebDriverWait(self._browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )

    def input_login(self, login: str):
        """
        Вводит логин пользователя в поле #user-name.

        :param login: str - Логин пользователя (например, 'standard_user').
        :return: None
        """
        input_username = self._browser.find_element(
            By.CSS_SELECTOR, "#user-name"
        )
        input_username.clear()
        input_username.send_keys(login)

    def input_password(self, password: str):
        """
        Вводит пароль пользователя в поле #password.

        :param password: str - Пароль пользователя (например, 'secret_sauce').
        :return: None
        """
        input_password = self._browser.find_element(
            By.CSS_SELECTOR, "#password"
        )
        input_password.clear()
        input_password.send_keys(password)

    def press_button_login(self):
        """
        Нажимает кнопку входа в систему (Login).

        :return: None
        """
        button_login = self._browser.find_element(
            By.CSS_SELECTOR, "#login-button"
        )
        button_login.click()

    def add_the_desired_items_to_the_cart(self):
        """
        Добавляет три конкретных товара в корзину:
        рюкзак, футболку и комбинезон.

        :return: None
        """
        add_backpack = self._browser.find_element(
            By.CSS_SELECTOR,
            "#add-to-cart-sauce-labs-backpack"
        )
        add_backpack.click()

    def go_in_cart(self):
        """
        Переходит в корзину (открывает модальное окно)
         и ждет появления кнопки Checkout.

        :return: None
         """
        cart_icon = self._browser.find_element(
            By.CSS_SELECTOR,
            ".shopping_cart_link"
        )
        cart_icon.click()


def press_button_checkout(self):
    """
    Нажимает кнопку 'Checkout' на странице корзины для перехода
    к оформлению заказа.

    :return: None
     """
    checkout_btn = self._browser.find_element(
        By.CSS_SELECTOR,
        "#checkout"
    )
    checkout_btn.click()


def input_first_name(self, first_name: str):
    """
    Вводит имя получателя на этапе оформления заказа.

    :param first_name: str - Имя получателя.
    :return: None
     """
    first_name_field = self._browser.find_element(
        By.CSS_SELECTOR,
        "#first-name"
    )
    first_name_field.clear()
    first_name_field.send_keys(first_name)


def get_itog_sum(self) -> str:
    """
    Получает итоговую сумму заказа из корзины.


    :return: str - Итоговая сумма как строка (например, "$58.29").
     """
    total_element = self._browser.find_element(
        By.CSS_SELECTOR,
        "[data-test='total-label']"
    )
    return total_element.text
