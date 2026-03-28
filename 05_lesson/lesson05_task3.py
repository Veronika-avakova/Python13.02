from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    try:
        # Загрузка страницы
        driver.get("http://the-internet.herokuapp.com/inputs")

        # Поиск поля ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # Ввод текста 12345
        input_field.send_keys("12345")
        time.sleep(2)  # Пауза

        # Очистка поля
        input_field.clear()
        time.sleep(2)  # Пауза

        # Ввод нового текста 54321
        input_field.send_keys("54321")
        time.sleep(2)  # Пауза

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
