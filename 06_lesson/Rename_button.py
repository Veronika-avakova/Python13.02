from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Настройка драйвера
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Перейти на нужную страницу
    driver.get('http://uitestingplayground.com/textinput')

    # Найти поле ввода и дождаться его готовности
    input_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'input'))
    )

    # Прокрутить экран к полю ввода
    driver.execute_script("arguments[0].scrollIntoView();", input_field)

    # Отправить текст в поле ввода
    input_field.send_keys('SkyPro')

    # Получить и вывести текст из кнопки
    button = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
    result_text = button.text.strip()
    print(result_text)

finally:
    # Завершить работу браузера
    driver.quit()
