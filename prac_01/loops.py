# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()
#
# numer_star = int(input('number of stars: '))
# for i in range(0, numer_star):
#     print('*', end=' ')
# print()

numer_star = int(input('number of stars: '))
count = 1
for i in range(0, numer_star + 1):

    print('*' * i)

print()