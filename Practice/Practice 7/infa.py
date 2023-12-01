def inf(file):
    with open(file, mode='r', encoding='utf-8') as text:
        st = text.read().splitlines()
    spst = [x.split('|') for x in st]
    return spst


def books(word, spst):
    slist = []
    for st in spst:
        if word in st[1]:
            slist.append(st)
    return slist


def total(list):
    numlist = []
    for el in list:
        if (int(el[3]) * float(el[4])) < 500:
            numlist.append((el[0], int(el[3]) * float(el[4]) + float(100)))
        else:
            numlist.append((el[0], int(el[3]) * float(el[4])))
    return numlist