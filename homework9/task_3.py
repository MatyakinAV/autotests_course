# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

import re
import heapq
with open('test_file/task_3.txt', encoding='utf-8') as file:
    lst = []
    summa_cheka = 0
    file_line = list(file.readlines())
    for i in file_line:
        if i != '\n':
            summa_cheka += int(i)
        else:
            lst.append(summa_cheka)
            summa_cheka = 0
three_most_expensive_purchases = sum(heapq.nlargest(3, lst))


assert three_most_expensive_purchases == 202346