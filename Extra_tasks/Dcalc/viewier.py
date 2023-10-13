import dcalc


def create_list(*args, **kwargs):
    a = []
    for q in range(len(args)):
        a.append(f'Point_{q} = {dcalc.deg_to_gms(args[q])}')
    for q, p in kwargs.items():
        a.append(f'{q} = {dcalc.deg_to_gms(p)}')
    return a


print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706448))