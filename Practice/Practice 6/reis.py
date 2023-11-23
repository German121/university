import re


def add_reis(a):
    dedd = re.compile("Рейс (\d+) (отправился|прибыл) (из|в) (\w+) в (\d+):(\d+):(\d+)")
    for m in dedd.finditer(a):
        nett = dedd.sub(fix_date, a)
        return nett


def fix_date(m):
    return f"[{m.group(5)}:{m.group(6)}:{m.group(7)}] - Поезд № {m.group(1)} {m.group(3)} {m.group(4)} "


def reis(file):
    inform = file.read().splitlines()
    with open("new.txt", mode="w", encoding="utf8") as new:
        new.write('')
    for strr in inform:
        newff = (add_reis(strr))
        if newff != None:
            with open("new.txt", mode="a", encoding="utf8") as new:
                new.write(f"{add_reis(strr)}\n")


file = open('infa.txt', mode='r', encoding='utf-8')