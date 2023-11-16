import os


def processing():
    try:
        name = input('Введите имя файла, из которого хотите импортировать данные: ').strip()
        f = open(f"{name}.txt")
        n = int(f.readline())
        sds = [int(f.readline()) for x in range(n)]
        f.close()
        return sds
    except FileNotFoundError:
        print("Файл не найден! Введите название заново! ")
        return processing()
    except OSError:
        print("Ошибка операционной системы!")
        return processing()
    except ValueError:
        print("В файле есть специальные символы!")
        return processing()
    except:
        print("Непредвиденная ошибка!")
        return processing()