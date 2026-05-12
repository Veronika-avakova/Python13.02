import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.pages.form_page import FormPage


@pytest.fixture(scope="function")
def browser():
    # Создаем сервис для управления драйвером
    service = Service(ChromeDriverManager().install())

    # Создаем опции браузера (можно настроить дополнительные параметры)
    options = webdriver.ChromeOptions()

    # Создаем экземпляр драйвера с сервисом и опциями
    driver = webdriver.Chrome(service=service, options=options)

    # Возвращаем драйвер для использования в тестах
    yield driver

    # Завершаем работу драйвера после выполнения теста
    driver.quit()


@allure.title("Проверка валидации формы")
@allure.description("Тест проверяет подсветку полей"
                    " при отправке формы с пустым ZIP-кодом.")
@allure.feature("Валидация формы")
@allure.severity(allure.severity_level.NORMAL)
def test_illumination_in_form(browser):
    form_page = FormPage(browser)

    with allure.step("Открыть страницу с формой"):
        form_page.open_form()

    with allure.step("Заполнить поля формы (оставить ZIP-код пустым)"):
        form_page.send_first_name("Иван")
        form_page.send_last_name("Петров")
        form_page.send_address("Ленина, 55-3")
        form_page.send_email("test@skypro.com")
        form_page.send_phone("+7985899998787")
        form_page.send_zip_code("")  # Оставляем пустым для ошибки!
        form_page.send_city("Москва")
        form_page.send_country("Россия")
        form_page.send_job_position("QA")
        form_page.send_company("SkyPro")

    with allure.step("Отправить форму"):
        form_page.press_button_submit()

    # Проверки (Assertions)
    with allure.step("Проверить наличие красной подсветки у поля ZIP-кода"):
        r_cl = form_page.get_class_red()
        assert "alert-danger" in r_cl, (f"В поле нет класса alert-danger. "
                                        f"Текущий класс: {r_cl}")

    with allure.step("Проверить количество зеленых полей (9 шт.)"):
        len_green_fields = form_page.get_class_green()
        assert len_green_fields == 9, (f"Ожидается 9 зеленых "
                                       f"полей, но найдено {len_green_fields}")
