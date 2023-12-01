from english_learn import *


def show():
    list = get_words()
    print(list)
    imenit = (normal(list))
    print(imenit)
    d = count(imenit)
    print(d)
    slist = (sort_words(d))
    print(slist)
    dictionary = translate_words(slist)
    with open('dictionary.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Исходное слово', 'Перевод', 'Количество упоминаний'])
        for i in dictionary:
            writer.writerow(i)
    print('Словарь успешно создан!')


if __name__ == "__main__":
    show()