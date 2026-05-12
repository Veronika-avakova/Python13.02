from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """
    Класс-страница для взаимодействия с интернет-магазином SauceDemo.
    Объединяет логику авторизации, работы с корзиной и оформления заказа.
    """

    def __init__(self, browser):
        self._browser = browser
        self._browser.maximize_window()

    def open_page_authorization(self):
        self._browser.get("https://www.saucedemo.com/")
        WebDriverWait(self._browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )

    def input_login(self, login: str):
        field = self._browser.find_element(By.CSS_SELECTOR, "#user-name")
        field.clear()
        field.send_keys(login)

    def input_password(self, password: str):
        field = self._browser.find_element(By.CSS_SELECTOR, "#password")
        field.clear()
        field.send_keys(password)

    def press_button_login(self):
        self._browser.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_the_desired_items_to_the_cart(self):
        """
        Добавляет три товара: рюкзак ($29.99), футболку ($15.99),
        комбинезон ($7.99). Итого с налогом: $58.29.
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    def go_in_cart(self):
        self._browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()

    def press_button_checkout(self):
        self._browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    def input_first_name(self, first_name: str):
        field = self._browser.find_element(By.CSS_SELECTOR, "#first-name")
        field.clear()
        field.send_keys(first_name)

    def input_last_name(self, last_name: str):
        field = self._browser.find_element(By.CSS_SELECTOR, "#last-name")
        field.clear()
        field.send_keys(last_name)

    def input_postal_code(self, postal_code: str):
        field = self._browser.find_element(By.CSS_SELECTOR, "#postal-code")
        field.clear()
        field.send_keys(postal_code)

    def press_button_continue(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
        ).click()

    def get_itog_sum(self) -> str:
        """
        Ожидает появления итоговой суммы и возвращает её значение.
        Элемент содержит текст вида "Total: $58.29" —
        метод отрезает префикс и возвращает только "$58.29".
        """
        total_element = WebDriverWait(self._browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='total-label']")
            )
        )
        return total_element.text.split(": ")[-1]
