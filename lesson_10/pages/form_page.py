from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """
    Класс-страница для взаимодействия с формой ввода данных.
    """

    def __init__(self, browser):
        """
        Инициализация страницы.

        :param browser: Экземпляр WebDriver (браузера).
        """
        self._browser = browser
        self._browser.maximize_window()

    def open_form(self):
        """
        Открывает страницу с формой и ждет загрузки основного блока.

        :return: None
        """
        self._browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main"))
        )

    # Методы для ввода данных в поля формы
    def send_first_name(self, first_name):
        """
        Вводит имя в соответствующее поле.

        :param first_name: str - Имя пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)

    def send_last_name(self, last_name):
        """
        Вводит фамилию в соответствующее поле.

        :param last_name: str - Фамилия пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)

    def send_address(self, address):
        """
        Вводит адрес в соответствующее поле.

        :param address: str - Адрес пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(address)

    def send_email(self, email):
        """
        Вводит e-mail в соответствующее поле.

        :param email: str - Электронная почта пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)

    def send_phone(self, phone):
        """
        Вводит номер телефона в соответствующее поле.

        :param phone: str - Номер телефона пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    def send_zip_code(self, zip_code):
        """
        Вводит ZIP-код в соответствующее поле.

        :param zip_code: str - Почтовый индекс.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)

    def send_city(self, city):
        """
        Вводит город в соответствующее поле.

        :param city: str - Город пользователя.
        :return: None
         """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(city)

    def send_country(self, country):
        """
        Вводит страну в соответствующее поле.

        :param country: str - Страна пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(country)

    def send_job_position(self, job_position):
        """
        Вводит должность в соответствующее поле.

        :param job_position: str - Должность пользователя.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)

    def send_company(self, company):
        """
        Вводит название компании в соответствующее поле.

        :param company: str - Название компании.
        :return: None
        """
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(company)

    def press_button_submit(self):
        """
        Нажимает кнопку отправки формы (Submit).

        :return: None
        """
        self._browser.find_element(By.CSS_SELECTOR, ".mt-3").click()

    # Методы для проверки валидации
    def get_class_red(self):
        """
        Получает значение атрибута 'class' для поля ZIP-кода
        (используется для проверки подсветки ошибки).

        :return: str - Значение атрибута class
        (например, 'form-control is-invalid').
        """
        classs = self._browser.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return classs

    def get_class_green(self):
        """
        Получает количество полей с зеленой подсветкой (успешная валидация).

        :return: int - Количество элементов с классом 'alert-success'.
         """
        green_fields = self._browser.find_elements(
            By.CSS_SELECTOR, ".alert-success")
        return len(green_fields)
