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

class PersonInfo:
    def __init__(self, fi: str, age: int, *args: list):
        self.fi = fi
        self.age = age
        self.way = [*args]

    def short_name(self):
        fam = []
        fam = self.fi.split(' ')
        return f"{fam[1]} {fam[0][0]}."

    def path_deps(self):
        stroka1 = ''

        for j in range(len(self.way)):
            if j < len(self.way) - 1:
                stroka1 = stroka1 + ''.join(f'{self.way[j]} --> ')
            else:
                stroka1 = stroka1 + ''.join(f'{self.way[j]}')
        return stroka1

    def new_salary(self):
        our_str = ''
        letters_dict = {}
        q = 0  # кол-во повторений
        summa_povtor = 0
        for v in self.way:
            our_str = our_str + ''.join(self.way)
        for k in our_str:
            if letters_dict.get(k) is None:  # если такого значения нет
                letters_dict.update({k: 1})  # вписываем ключ и значение 1 в словарь
            else:
                q = letters_dict.get(k)  # записываем кол-во повторений буквы + 1
                letters_dict.update({k: q + 1})  # записываем в словарь новое значение к ключу

        sorted_dict = sorted(letters_dict.items(), key=lambda x: x[1])
        #top3 = sorted(updated, key=operator.itemgetter(1), reverse=True)[:3]
        return 1337 * self.age * summa_povtor



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
