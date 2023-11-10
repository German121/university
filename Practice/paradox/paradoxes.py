import random


def monty_hall(n):
    choice_1_win = 0  # количестов побед, когда игрок согласился изменить выбор
    choice_2_win = 0  # количестов побед, когда игрок не согласился изменить выбор
    win_count = 0
    for i in range(n):
        priz_place = random.randrange(1, 4)
        computer_choice = random.randrange(1, 4)
        leader_choice = [i for i in range(1, 4) if
                         i != priz_place and i != computer_choice][0]  # ведущий выбрал дверь, где точно нет приза
        choice_2 = random.choice([1, 0])  # 1 - да, 0 - нет (игрок делает выбор: сменить дверь или нет)
        if choice_2:
            if (6 - computer_choice - leader_choice) == priz_place:  # проверка второго выбора игрока
                choice_2_win += 1
                win_count += 1
        else:
            if computer_choice == priz_place:
                choice_1_win += 1
                win_count += 1
    return f'Шанс выиграть, не изменив выбор: {round(choice_1_win / win_count * 100, 2)}%\n' \
           f'Шанс выиграть, изменив выбор: {round(choice_2_win / win_count * 100, 2)}%\n' \
           f'Шанс увеличится на {round(choice_2_win / win_count * 100 - choice_1_win / win_count * 100, 2)}%\n'


def couples(dates):
    k = 0
    for i in range(len(dates)):
        for j in range(i + 1, len(dates)):
            if dates[i] == dates[j]:
                k += 1
                return k


def birthday(kol_group1, kol_group2, kol_prog):
    count1 = 0
    count2 = 0
    for l in range(kol_prog):
        dates_1 = [random.randint(0, 365) for i in range(kol_group1)]
        dates_2 = [random.randint(0, 365) for i in range(kol_group2)]
        c1 = couples(dates_1)
        c2 = couples(dates_2)
        if c1:
            count1 += 1
        if c2:
            count2 += 1
    return f'Вероятность совпадения в группе из {kol_group1} чел.: {round(count1 / kol_prog * 100, 2)}%\n' \
           f'Вероятность совпадения в группе из {kol_group2} чел.: {round(count2 / kol_prog * 100, 2)}%\n'
