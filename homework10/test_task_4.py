# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from datetime import datetime

@pytest.mark.usefixtures('time_calculation_class')
class Test_Exponentiation:

    def test_time_calculation(self):
        quantity = 0
        for i in range(100000000):
            quantity += i ** 2

    def test_time_calculation2(self, time_calculation_method):
        quantity = 0
        for i in range(100000000):
            quantity += i ** 3