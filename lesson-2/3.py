# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


# решение через словарь
seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
print('Решение через тип данных - dict:')
user_month = int(input('Введите номер месяца в году: '))
while user_month < 1 or user_month > 12:
    print('Необходимо ввести число от 1 до 12')
    user_month = int(input('Повторите ввод номера месяца в году: '))
else:
    for i in seasons.items():
        if user_month in i[1]:
            print(f'Время года введённого месяца({user_month}) - {i[0]}')
            break


# решение через список
seasons = [
    [1, 'Зима'],
    [2, 'Зима'],
    [3, 'Весна'],
    [4, 'Весна'],
    [5, 'Весна'],
    [6, 'Лето'],
    [7, 'Лето'],
    [8, 'Лето'],
    [9, 'Осень'],
    [10, 'Осень'],
    [11, 'Осень'],
    [12, 'Зима'],
]
print('Решение через тип данных - list:')
user_month = int(input('Введите номер месяца в году: '))
while user_month < 1 or user_month > 12:
    print('Необходимо ввести число от 1 до 12')
    user_month = int(input('Повторите ввод номера месяца в году: '))
else:
    for i in seasons:
        if user_month in i:
            print(f'Время года введённого месяца({user_month}) - {i[1]}')
            break