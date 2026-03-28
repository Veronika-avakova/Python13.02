from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Создаем экземпляр драйвера
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Переходим на тестовую страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
               "loading-images.html")

    # Ждём, пока загрузятся все изображения
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Ждём, пока загрузятся минимум 3 изображения
    WebDriverWait(driver, 10).until(
        lambda drv: len(drv.find_elements(By.TAG_NAME, "img")) >= 3
    )

    # Получаем список всех изображений
    images = driver.find_elements(By.TAG_NAME, "img")

    # Проверяем, что найдено минимум 3 изображения
    if len(images) >= 3:
        # Получаем атрибут src третьего изображения
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("Third.")  # Сообщение, если изображений менее 3-х

finally:
    # Закрываем браузер
    driver.quit()