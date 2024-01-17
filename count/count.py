with open('joinDate.txt', 'r', encoding='utf-8') as r:
    with open('joinDate2.txt', 'a', encoding='utf-8') as w:
        for line in r:
            w.write(line[:11]+'\n')

