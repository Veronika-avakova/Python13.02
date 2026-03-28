from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                install()))

driver.get("http://www.uitestingplayground.com/ajax")

wait = WebDriverWait(driver, 20)
ajax_button = wait.until(
    EC.element_to_be_clickable((By.ID, "ajaxButton"))
)
ajax_button.click()

success_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

print(success_message.text)

driver.quit()
