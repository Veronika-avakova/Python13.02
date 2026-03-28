import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from chromedriver_autoinstaller import install


def main():
    # Устанавливаем Chromedriver
    driver = webdriver.Chrome(service=Service(install()))

    try:
        # Переходим на тестовую страницу
        driver.get('http://uitestingplayground.com/classattr')

        # Ждем появления кнопки с нужным классом
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )

        # Кликаем на кнопку
        button.click()

        print("Кнопка успешно нажата!")

    finally:
        # Пауза перед закрытием окна браузера
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    main()
