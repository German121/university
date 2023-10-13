import dcalc


def create_list(*args, **kwargs):
    arr = []
    for i in range(len(args)):
        arr.append(f'Point_{i} = {dcalc.deg_to_gms(args[i])}')
    for i, j in kwargs.items():
        arr.append(f'{i} = {dcalc.deg_to_gms(j)}')
    return arr


print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706448))