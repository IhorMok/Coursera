# points = [(1, 1),
#           (5, 1),
#           (10, 10)
#           ]
# points.sort(key=lambda p: p[0]**2 + p[1]**2)
# print(*points)

#=====================
# x = [1, 5, 2, 3]
# y = list(map(lambda x: x**2, x))
# print(*y)

#======next_lesson==
# def printList(lst, mySep=' '):
#     for i in range(len(lst) - 1):
#         print(lst[i], mySep, sep='', end='')
#     print(lst[-1], sep='')
# printList([1, 2, 3], mySep='a')
# printList([5, 6, 7])

#=============
# def mySum(*args):
#     nowSum = 0
#     for now in args:
#         nowSum += now
#     return nowSum
# print(mySum(1, 2, 3, 4))
# print(mySum(1))

#=======
def myMin(first, *others):
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin
print(myMin(5, 2, 3, 4))
