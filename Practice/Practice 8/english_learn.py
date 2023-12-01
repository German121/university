import pymorphy3
import pymorphy3_dicts_ru
import translate
from translate import Translator
import csv


def get_words():
    f = open('input.txt', mode="r", encoding="utf8")
    st = f.read().splitlines()
    f.close()
    stlist = [st[i].split(' ') for i in range(len(st))]
    clear_list = []
    for i in range(len(stlist)):
        for word in stlist[i]:
            word = ''.join(filter(str.isalpha, word)).lower()
            if len(word) > 0:
                clear_list.append(word)
    return clear_list


def normal(clear_list):
    imenit = []
    for word in clear_list:
        morph = pymorphy3.MorphAnalyzer()
        imenit.append(morph.parse(word)[0].normal_form)
    return imenit


def count(imenit):
    d = {}
    for i in range(len(imenit)):
        if not imenit[i] in d:
            d[imenit[i]] = 1
        else:
            d[imenit[i]] += 1
    return d


def sort_words(d):
    sorted_d = sorted(d.items(), key=lambda kv: kv[1])
    sorted_d.reverse()
    return sorted_d


def translate_words(sorted_list):
    translate_dictionary = []
    for i in range(len(sorted_list)):
        translation = Translator(from_lang='ru', to_lang="en").translate(str(sorted_list[i][0]))
        translate_dictionary.append([sorted_list[i][0], translation, sorted_list[i][1]])
        print(f'Переведено {i}/{len(sorted_list)}...')
    return translate_dictionary