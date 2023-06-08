# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

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


@pytest.mark.parametrize('l, result', [([9, 3, 3], 1.0), ([6, 3, 1], 2.0), ([6, 6, 1], 1.0)])
def test12(l, result):
    assert all_division(*l) == result


@pytest.mark.skip('разработчик не сделал проверку на  строку!')
def test4():
    assert all_division('asdasdasd') == 1, 'невозможно разделить т.к. указана строка'


def test5():
    assert all_division(0, 1) == 0
