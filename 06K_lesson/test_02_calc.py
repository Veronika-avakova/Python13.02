import pytest
import time  # Добавлен импорт time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)
    wait = WebDriverWait(driver, 60)

    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay'))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="7"]'))
    )
    driver.execute_script("arguments[0].click()", button_7)

    button_plus = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="+"]'))
    )
    driver.execute_script("arguments[0].click()", button_plus)

    button_8 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="8"]'))
    )
    driver.execute_script("arguments[0].click()", button_8)

    button_equals = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="="]'))
    )
    driver.execute_script("arguments[0].click()", button_equals)

    time.sleep(45)

    result_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "screen"))
    )
    assert result_element.text.strip() == "15", "Результат не равен 15"
