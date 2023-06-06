# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

import re
with open("test_file/task1_answer.txt", 'a+', encoding='utf-8') as file1:
    with open("test_file/task1_data.txt", encoding='utf-8') as file:
        a = True
        while a:
            file_line = file.readline()
            s1 = re.sub("\n", "", file_line)
            file1.write(s1)
            if not file_line:
                a = False
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')