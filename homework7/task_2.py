# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
from collections import Counter


class PersonInfo:
    def __init__(self, fi: str, age: int, *args: list):
        """
        Класс персональных данных
        :param fi: Фамилия имя типа str
        :param age: Возраст типа int
        :param args: Путь подразделенеия где работает сотрудник
        """
        self.fi = fi
        self.age = age
        self.way = [*args]

    def short_name(self):
        """
        Метод палучениния из Фамилии Имени, Фамилии И.
        :return: Фамилия И.
        """
        fam = []
        fam = self.fi.split(' ')
        return f"{fam[1]} {fam[0][0]}."

    def path_deps(self):
        """
        Возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
        :return: Строку с данными типа : Головное подразделение --> ... --> Конечное подразделение
        """
        path = ''

        for j in range(len(self.way)):
            if j < len(self.way) - 1:
                path = path + ''.join(f'{self.way[j]} --> ')
            else:
                path = path + ''.join(f'{self.way[j]}')
        return path

    def new_salary(self):
        """
        Метотод вычисляет новую зарплату по формуле: 1337* Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
        :return: 1337 * Age * amount_of_repeats ( суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений )
        """
        our_str = ''
        popular = 3
        amount_of_repeats = 0
        for j in self.way:
            our_str = our_str + ''.join(j)
        our_str = list(our_str)
        cnt = (Counter(our_str)).most_common(popular)
        for k in range(popular):
            amount_of_repeats += cnt[k][1]
        return 1337 * self.age * amount_of_repeats


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]

test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
