from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()

    try:
        # Загрузка страницы
        driver.get("http://uitestingplayground.com/dynamicid")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-primary"))
        )

        # Клик по кнопке
        button.click()

        # Пауза
        time.sleep(3)

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
