class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    @staticmethod
    def capitalize(string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст.
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    @staticmethod
    def trim(string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале и конце строки.
        Пример: `trim("   skypro") -> "skypro"`
        """
        return string.strip()

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
         (регистр не важен),
        и `False` - если нет.
        Параметры:
            `string` - строка для обработки
        """
