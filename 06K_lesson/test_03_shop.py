from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
        )
    driver.get(
        "https://www.saucedemo.com/"
        )
    driver.maximize_window()

# авторизация
    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

# добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )

    driver.find_element(By.ID, "checkout").click()

# заполнение формы
    driver.find_element(By.ID, "first-name").send_keys('Вероника')
    driver.find_element(By.ID, "last-name").send_keys('Бова')
    driver.find_element(By.ID, "postal-code").send_keys('350000')

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )

    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert total == "Total: $58.29"

    driver.quit()
