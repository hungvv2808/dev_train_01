# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# while y < x:
#     y = int(input('Re-enter y (y > x): '))
x, y = 1, 10


# def getMinStep(x, y):
#     countStep = 0
#     logsCase = ''
#     print('-' * 10 + 'Case and current value' + '-' * 10)
#     while True:
#         if x * 2 <= y:
#             x *= 2
#             print(f'(*2) x = {x}, y = {y}')
#             logsCase += ' * 2)'
#         elif x * 2 > y:
#             if y % 2 == 1:
#                 x *= 2
#                 print(f'(*2) x = {x}, y = {y}')
#                 logsCase += ' * 2)'
#             else:
#                 x -= 1
#                 print(f'(-1) x = {x}, y = {y}')
#                 logsCase += ' - 1)'
#         else:
#             input('Cannot find the case to math !')
#
#         # check case by case
#         # input('Press enter to continue')
#         countStep += 1
#
#         if x == y:
#             return countStep, logsCase


def minimumOperator(x, y):
    if x == y:
        return 0
    # only way is to do
    # -1(x - y): times
    if x > y:
        return x - y
    # not possible
    if x <= 0 and y > 0:
        return -1
    # y is greater and y is odd
    if y % 2 == 1:
        # perform '-1' on x
        # (or +1 on y):
        print(' - 1 ')
        return 1 + minimumOperator(x, y + 1)
        # y is even
    else:
        # perform '*2' on x
        # (or y/2 on y):
        print(' * 2 ')
        return 1 + minimumOperator(x, y / 2)


print('Note: Read logs backwards from the bottom up will make the correct answer !!!')
print('Min step: %d' % minimumOperator(x, y))

# print(f'Default value: x = {x}, y = {y}')
# count_step, logsCase = getMinStep(x, y)
# print('-' * 15 + ' Result ' + '-' * 15)
# print(f'Min step: {count_step}')
# print('Case list logs: %s%d%s = %d' % ('(' * count_step, x, logsCase, y))
