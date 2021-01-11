x = int(input('Enter x: '))
y = int(input('Enter y: '))
while y < x:
    y = int(input('Re-enter y (y > x): '))
# x, y = 1, 10


def getMinStep(x, y):
    countStep = 0
    logsCase = ''
    print('-'*10 + 'Case and current value' + '-'*10)
    while True:
        if x * 2 <= y:
            x *= 2
            print(f'(*2) x = {x}, y = {y}')
            logsCase += ' * 2 '
        elif x * 2 > y:
            if y % 2 == 1:
                x *= 2
                print(f'(*2) x = {x}, y = {y}')
                logsCase += ' * 2 '
            else:
                x -= 1
                print(f'(-1) x = {x}, y = {y}')
                logsCase += ' - 1 '
        else:
            input('Cannot find the case to math !')

        # check case by case
        # input('Press enter to continue')
        countStep += 1

        if x == y:
            return countStep, logsCase


print(f'Default value: x = {x}, y = {y}')
count_step, logsCase = getMinStep(x, y)
print('-'*15 + ' Result ' + '-'*15)
print(f'Min step: {count_step}')
print('Case list logs: ' + logsCase)
