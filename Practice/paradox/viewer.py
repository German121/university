from paradoxes import birthday, monty_hall


def show():
    while True:
        a = input('1. Запуск Monty_Hall\n2. Запуск Birthday\n3. Выход\n')
        if a == '1':
            try:
                print((monty_hall(int(input('Введите кол-во экспериментов: ')))))
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(10000)')
                print(monty_hall(10000))
        if a == '2':
            try:
                kol1 = int(input('Введите количество учеников в 1-ой группе: '))
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(23)')
                kol1 = 23
            try:
                kol2 = int(input('Введите количество учеников во 2-ой группе: '))
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(60)')
                kol2 = 60
            try:
                kol3 = int(input('Введите количество экспериментов: '))
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(1000)')
                kol3 = 1000
            print(birthday(kol1, kol2, kol3))
        if a == '3':
            break