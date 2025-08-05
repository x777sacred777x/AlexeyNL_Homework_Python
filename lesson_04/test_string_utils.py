import pytest
from string_utils import StringUtils

# Инициализация объекта для тестирования
string_utils = StringUtils()

# Тесты для метода capitalize


@pytest.mark.capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),            # Обычная строка
    ("hello world", "Hello world"),  # Строка с пробелом
    ("python", "Python"),            # Одно слово
    ("тест", "Тест"),                # Кириллица
    ("123abc", "123abc"),            # Числа в начале
    ("a", "A"),                      # Один символ
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                        # Пустая строка
    ("   ", "   "),                  # Пробелы
    ("123", "123"),                  # Только цифры
    ("!test", "!test"),             # Спецсимвол в начале
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для метода trim


@pytest.mark.trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),         # Несколько пробелов
    ("  hello world", "hello world"),  # Пробелы перед фразой
    ("    python", "python"),        # Много пробелов
    ("  тест", "тест"),              # Кириллица
    (" \t\nword", "\t\nword"),       # Символы табуляции и переноса
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                        # Пустая строка
    ("skypro", "skypro"),            # Нет пробелов
    ("123", "123"),                  # Числовая строка
    ("test   ", "test   "),          # Пробелы в конце
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для метода contains


@pytest.mark.contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),           # Первый символ
    ("SkyPro", "k", True),           # Символ в середине
    ("SkyPro", "o", True),           # Последний символ
    ("тест", "т", True),             # Кириллица
    ("hello world", " ", True),      # Пробел как символ
    ("123", "2", True),              # Цифра
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.contains
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),          # Отсутствующий символ
    ("SkyPro", " ", False),          # Пробел в строке без пробелов
    ("", "S", False),                # Пустая строка
    ("тест", "д", False),            # Отсутствующая кириллица
    ("123", "4", False),             # Отсутствующая цифра
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Тесты для метода delete_symbol


@pytest.mark.delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),        # Удаление одного символа
    ("SkyPro", "Pro", "Sky"),        # Удаление подстроки
    ("тест", "т", "ес"),             # Кириллица
    ("hello world", " ", "helloworld"),  # Удаление пробела
    ("banana", "na", "ba"),          # Множественное вхождение
    ("111", "1", ""),                # Удаление всех символов
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.delete_symbol
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),       # Отсутствующий символ
    ("", "S", ""),                   # Пустая строка
    ("тест", "д", "тест"),           # Отсутствующая кириллица
    ("123", "4", "123"),             # Отсутствующая цифра
    ("test", "", "test"),            # Пустая подстрока
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

# Дополнительные тесты на граничные случаи


@pytest.mark.xfail
def test_capitalize_with_none():
    """Проверка реакции на None (ожидаем падение теста)"""
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.xfail
def test_contains_with_none():
    """Проверка реакции на None (ожидаем падение теста)"""
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")
