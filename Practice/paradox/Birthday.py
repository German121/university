import random


def pari(dt):
    k = 0
    for a in range(len(dt)):
        for b in range(a + 1, len(dt)):
            if dt[a] == dt[b]:
                k += 1
    return k


def birthday(n):
    c23 = 0
    c60 = 0
    for l in range(n):
        dt_23 = [(random.randrange(1, 29), random.randrange(1, 13)) for b in range(23)]
        dt_60 = [(random.randrange(1, 29), random.randrange(1, 13)) for b in range(60)]
        cc23 = pari(dt_23)
        cc60 = pari(dt_60)
        if cc23:
            c23 += 1
        if cc60:
            c60 += 1
    return f'Вероятность совпадения в группе из 23 человек: {int(c23 / n * 100)}%\nВероятность совпадения в группе из 60 человек: {int(c60 / n * 100)}%'