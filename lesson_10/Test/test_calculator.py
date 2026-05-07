
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.pages.calculator_page import CalculatorPage
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    service = Service(ChromeDriverManager().install())  # Создаем сервис
    options = webdriver.ChromeOptions()  # Создаем опции

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора")
@allure.description("Тест проверяет вычисление 7 + 8 с задержкой ответа.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def click_button_equal(self):
    """
    Нажимает кнопку "=" на калькуляторе и возвращает время ожидания.

    :return: float - Время ожидания результата.
    """

    # Нажимаем кнопку "="
    equal_button = self._browser.find_element(By.CSS_SELECTOR, "#equal-button")
    equal_button.click()


def test_result_15_after_45_seconds(browser):
    calculator_page = CalculatorPage(browser)

    with allure.step("Открыть калькулятор"):
        calculator_page.open_calculator()

    with allure.step("Установить задержку ответа на 3 секунды"):
        input_text = calculator_page.fill_form(3)

    with allure.step("Ввести число 7"):
        calculator_page.click_button_7()

    with allure.step("Нажать оператор +"):
        calculator_page.click_button_plus()

    with allure.step("Ввести число 8"):
        calculator_page.click_button_8()

    with allure.step("Нажать равно и получить время ожидания"):
        waiting_time = calculator_page.click_button_equal()

    with allure.step("Получить результат вычисления"):
        result_in_window = calculator_page.get_result()

    # Проверки (Assertions)
    with allure.step("Проверить соответствие времени ожидания"):
        assert waiting_time == input_text, (f"Ошибка. "
                                            f"Введенное время: {input_text}, "
                                            f"время ожидания: {waiting_time}")

    with (allure.step("Проверить результат вычисления")):
        assert result_in_window == "15", (f"Ожидалось 15,"
                                          f" а в ответе - {result_in_window}")
