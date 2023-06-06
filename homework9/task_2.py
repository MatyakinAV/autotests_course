# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


from datetime import datetime, time
from pathlib import Path
import time


def func_log(file_log='log.txt'):
    """
    Дозаписывает в указанный файл(или по умолчанию) название вызываемой функции и дату и время вызова
    по формату д.м ч:м:с
    :param file_log: по умолчанию 'log.txt'
    :return:
    """
    def writer(func):
        def wrapper(*args, **kwargs):
            res_func = Path(Path.cwd(), file_log)  # вызов функции
            now = datetime.now(func())
            month = now.strftime("%m")
            day = now.strftime("%d")
            date_time = now.strftime("%d.%m %H:%M:%S")
            with open(res_func, "a+", encoding='utf-8') as file:
                file.write(f'{func.__name__} вызвана {date_time}\n')

        wrapper.__name__ = func.__name__  # вручную присваем данные по функции в нашем декораторе и после ретурна
        wrapper.__doc__ = func.__doc__  # получаем теже данные что и без декоратора
        wrapper.__wrapped__ = func
        return wrapper

    return writer


@func_log()
def func1():
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)


func1()
