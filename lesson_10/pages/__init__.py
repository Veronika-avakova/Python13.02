from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:
    """
    Класс-страница для взаимодействия с калькулятором на сайте.
    """

    def __init__(self, browser):
        """
        Инициализация страницы.

        :param browser: Экземпляр WebDriver (браузера).
        """
        self._browser = browser
        self._browser.maximize_window()

    def open_calculator(self):
        """
        Открывает страницу калькулятора и ждет загрузки основного блока.

        :return: None
        """
        self._browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html"
        )
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".col-sm-12.py-10")
            )
        )

    def fill_form(self, second):
        """
        Вводит значение в поле задержки (секунды).

        :param second: int - количество секунд для задержки.
        :return: int - значение, которое было введено в поле.
        """
        input_field = self._browser.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys(second)

        # Получаем значение из атрибута value и приводим к int
        input_text = int(self._browser.find_element(
            By.CSS_SELECTOR, "#delay").get_attribute("value"))
        return input_text

    def click_button_7(self):
        """
        Нажимает кнопку с цифрой '7'.

        :return: None
        """
        buttons = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        buttons[1].click()

    def click_button_plus(self):
        """
        Нажимает кнопку '+' (сложение).

        :return: None
        """
        buttons = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        buttons[4].click()

    def click_button_8(self):
        """
        Нажимает кнопку с цифрой '8'.

        :return: None
        """
        buttons = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        buttons[2].click()

    def click_button_equal(self):
        """
        Нажимает кнопку '=' и вычисляет время ожидания результата.

        :return: int - время в секундах, которое прошло
         до появления результата.
                 Возвращает округленное целое число.
                 Если результат не появился за 55 секунд,
                  тест упадет с TimeoutException.
                 """

        # Находим все кнопки и нажимаем на кнопку '=' (индекс 15)
        buttons = self._browser.find_elements(By.CSS_SELECTOR, ".btn")

        # Фиксируем время ДО нажатия
        start_time = time.time()

        buttons[15].click()

        # Ожидаем появления текста "15" на экране калькулятора
        waiter = WebDriverWait(self._browser, 55, 0.1)

        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        # Фиксируем время ПОСЛЕ появления результата
        end_time = time.time()

        # Вычисляем разницу и округляем до целого числа секунд
        waiting_time = int(end_time - start_time)
        return waiting_time


def get_result(self):
    """
    Получает текстовое значение результата с экрана калькулятора.

    :return: str - текст, отображаемый на экране (например, "15").
             """

    result_in_window = self._browser.find_element(
        By.CSS_SELECTOR, ".screen").text

    return result_in_window
