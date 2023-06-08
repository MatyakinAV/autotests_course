# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты
import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert all_division(2, 2) == 1.0


def test2():
    assert all_division(2, 0), 'нельзя делить на 0'


@pytest.mark.smoke
def test12():
    assert all_division(10, 2, 5) == 1.0


def test4():
    assert all_division('asdasdasd') == 1, 'невозможно разделить т.к. указана строка'


def test5():
    assert all_division(0, 1) == 0
