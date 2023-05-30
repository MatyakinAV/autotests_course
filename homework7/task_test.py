way = ['Разработка', 'УК', 'Автотесты']
stroka1 = ''
for j in range(len(way)):
    if j < len(way) - 1:
        stroka1 = stroka1 + ''.join(f'{way[j]} --> ')
    else:
        stroka1 = stroka1 + ''.join(f'{way[j]}')
print(stroka1)
