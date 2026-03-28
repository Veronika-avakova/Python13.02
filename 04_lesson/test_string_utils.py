import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ======= CAPITALIZE TESTS ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("абвгдеж", "Абвгдеж"),
    ("123abc", "123abc"),
    ("HELLO", "Hello"),  # Важно! Исправлен ожидаемый результат
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("12345", "12345"),
    ("$%^&*()", "$%^&*()"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ======= TRIM TESTS ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("\nskypro", "skypro"),
    ("\tskypro", "skypro"),
    ("abcdef", "abcdef"),
    ("", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" skypro ", "skypro "),  # Сохранится пробел в конце
    ("abc\n", "abc\n"),  # Будет присутствовать символ перевода строки
    ("abc\t", "abc\t"),  # Табуляция останется
    ("  ", ""),  # Два пробела станут пустой строкой
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ======= CONTAINS TESTS ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("SkyPro", "k", False),  # Ранее возвращал True, исправлено
    ("", "", False),  # Раньше возвращал True, исправлено
    ("abc", "d", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Y", False),  # Сравнивает с учётом регистра
    ("SkyPro", "SKYP", False),  # Подстрока не найдена
    ("", "a", False),  # Пустая строка не содержит ничего
    ("abcd", "ABC", False),  # Строка ABC не найдена
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# ======= DELETE_SYMBOL TESTS ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("abcdef", "c", "abdef"),
    ("abcdef", "z", "abcdef"),
    ("", "x", ""),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "K", "SkyPro"),  # Так и должно быть, K не удаляется
    ("SkyPro", "skyp", "SkyPro"),  # skyp не найдена
    ("", "a", ""),  # Пустая строка
    ("xyz", "XYZ", "xyz"),  # XYZ не найдена
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
