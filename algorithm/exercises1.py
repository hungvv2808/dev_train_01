def hun(exp, i):
    if i <= 9:
        for e in (' + ', ' - ', ''):
            hun(exp + e + str(i), i + 1)
    elif eval(exp) == 100:
        print('100 = ' + exp)


hun('1', 2)
