from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():

    driver = webdriver.Firefox()

    try:
        # Загрузка страницы
        driver.get("http://the-internet.herokuapp.com/login")

        # Заполнение полей формы
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("tomsmith")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Ожидание появления зелёной плашки
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
        )

        # Получение и вывод текста с зелёной плашки
        message_text = (
            success_message.text.strip()
        )
        print(f"Текст с зелёной плашки: {message_text}")

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
