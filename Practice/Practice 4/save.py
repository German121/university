def read_file(name):
    f = open(f"{name}", mode="r", encoding="utf8")
    st = f.read().splitlines()
    st_list = [st[i].split(' ') for i in range(len(st))]
    clear = []
    for i in range(len(st_list)):
        for word in st_list[i]:
            word = ''.join(filter(str.isalnum, word)).lower()
            if len(word) > 0:
                clear.append(word)
    w_s = set(clear)
    return sorted(w_s)

def save_file(name, words):
    new_text = open(f"{name}", mode='w', encoding='utf8')
    new_text.write(f"{(len(words))} \n")
    for i in range(len(words)):
        new_text.write(f"{(words[i])} \n")