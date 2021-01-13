x, y = 4, 9


def minimumOperator(x, y):
    if x == y:
        return 0
    if x > y:
        print(' - 1 ')
        return x - y
    if x <= 0 and y > 0:
        return -1
    if y % 2 == 1:
        print(' - 1 ')
        return 1 + minimumOperator(x, y + 1)
    else:
        print(' * 2 ')
        return 1 + minimumOperator(x, y / 2)


print('Note: Read logs backwards from the bottom up will make the correct answer !!!')
print('Min step: %d' % minimumOperator(x, y))
