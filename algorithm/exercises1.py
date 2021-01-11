def sumTo100(arrNum, i):
    if i <= 9:
        for act in (' + ', ' - ', ''):
            newArr = arrNum + act + str(i)
            # check side by side
            # print(f'Round {i}: arr = ' + newArr + f', i = {i}')
            sumTo100(newArr, i + 1)
    elif eval(arrNum) == 100:
        print('100 = ' + arrNum)


sumTo100('1', 2)
