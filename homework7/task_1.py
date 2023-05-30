# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

class Segment:
    def __init__(self, tochka1, tochka2):
        """
        Класс сегмент

        Переменные
        :type tochka1: кортеж1, точка отрезка 1
        :type tochka2: кортеж2, точка отрезка 2
        x1, y1 = координаты первой точки
        x2 , y2 = координаты второй точки

        """
        self.tochka1 = tochka1
        self.tochka2 = tochka2
        self.x1 = tochka1[0]
        self.y1 = tochka1[1]
        self.x2 = tochka2[0]
        self.y2 = tochka2[1]

    def length(self):
        """
        Метод поиска длины отрезка
        :return: возвращаем длинну с округлением до 2 знаков после запятой
        """

        d = round((((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5), 2)
        return d

    def x_axis_intersection(self):
        """
        Метод смотри , пересекает ли отрезок ось абсцисс
        :return: возвращаем True если пересекает, иначе False
        """
        if self.y1 * self.y2 < 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        Метод смотрит , пересекает ли отрезок ось ординат
        :return: возвращаем True если пересекает, иначе False
        """

        if self.x1 * self.x2 < 0:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
