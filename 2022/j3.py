s = input()
strings = ""
sign = ''
amount = ""
next = False
for i in range(len(s) + 1):
    if i == len(s) or next:
        signStr = "tighten" if sign == '+' else "loosen"
        print(strings, signStr, amount)
        strings = ""
        sign = ''
        amount = ""
        next = False
        if i == len(s): break
    c = s[i]
    if c in 'ABCDEFGHIJKLMNOPQRST':
        strings += c
    elif c in "+-":
        sign = c
    else:
        amount += c
        next = True
