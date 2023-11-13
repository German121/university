def get_words(path="words.txt"):
    text = open(path, encoding='utf8')
    text_list = text.read().upper().splitlines()
    text.close()
    return text_list


def get_records(record, path="records.txt"):
    record_file = open(path, mode="r+", encoding="utf8")
    cur_record = record_file.readline()
    if cur_record == '':
        cur_record = '0'
    cur_record = max(int(cur_record), int(record))
    record_file.seek(0)
    record_file.write(str(cur_record))
    return cur_record