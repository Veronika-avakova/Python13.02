from selenium import webdriver
from selenium.webdriver.common.by import By


def test_fill_form():
    driver = webdriver.Edge()

    try:
        (driver.get
         ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

        all_inputs = []

        inputs = driver.find_elements(By.TAG_NAME, "input")
        for i, inp in enumerate(inputs):
            print(f"Input {i}: {inp.get_attribute('name')}")
            all_inputs.append(inp.get_attribute('name'))

        # Заполнение полей
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Отправка формы
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Определение цветов для проверки
        green = 'alert-success'
        red = 'alert-danger'

        print("==Вывоб информации о полях после отправки==")

        # Проверка цветов полей
        color = len(all_inputs)
        for inp in all_inputs:
            tmp = driver.find_element(By.ID, inp)
            if green in tmp.get_attribute('class'):
                print(f"Поле {inp} - Зеленое: {tmp.text}")
            if red in tmp.get_attribute('class'):
                print(f"Поле {inp} - Красное: {tmp.text}")
                color -= 1

        # Утверждение
        assert len(all_inputs) == color, "Есть красные поля"

    except Exception as e:
        print(f"!!! => {e}")

    finally:
        driver.quit()


test_fill_form()
