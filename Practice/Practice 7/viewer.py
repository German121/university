from infa import *


def show():
    try:
        spst = (inf('info.csv'))
        name = input('Введите строку, с которой хотите книгу: ').strip()
        list = books(name, spst)
        sss = (total(list))
        if len(sss) == 0:
            print('Таких книг нет')
        else:
            print(sss)
    except:
        print('Ошибка')