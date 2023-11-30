key = int(input('ключ ='))
text = input('текст =')
list_text = list(text)
lenght = len(list_text)
process = ""

while key > 0:
    b = 0
    while b < lenght:
        h = b +1
        if h % key == 0:
            if list_text[b] != 0:
               process += list_text[b]
            list_text[b] = 0
        b += 1
    key -= 1

print('змінений текст =',process)
