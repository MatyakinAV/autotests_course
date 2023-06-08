import pytest
from datetime import datetime


@pytest.fixture(scope='class')
def time_calculation_class():
    startTime = datetime.now()
    print(f'Время начала выполнения класса {startTime}')
    yield startTime
    print(f'\nВремя окончания работы класса {datetime.now()}, класс выполнялся {datetime.now() - startTime}')


@pytest.fixture()
def time_calculation_method():
    startTime_method = datetime.now()
    print(f'Время начала выполнения метода {startTime_method}')
    yield startTime_method
    print(f'\nВремя выполнения теста {datetime.now() - startTime_method}')
