import random


def monty_hall(n):
    win1 = 0
    win2 = 0
    win_k = 0
    for a in range(n):
        priz = random.randrange(1, 4)
        computer = random.randrange(1, 4)
        empty_place = [b for b in range(1, 4) if b != priz and b != computer][0]
        choice_2 = random.choice([1, 0])
        if choice_2:
            if (6 - computer - empty_place) == priz:
                win2 += 1
                win_k += 1
        else:
            if computer == priz:
                win1 += 1
                win_k += 1
    return f'Шанс увеличится на {int(win2 / win_k * 100) - int(win1 / win_k * 100)} процента'
