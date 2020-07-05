p = int(input())
x = int(input())
y = int(input())
total = 100 * x + y
total_after = int(total * (100 + p) / 100)
print(total_after // 100, total_after % 100)



#=====================Quadratic_equation-1====РАЗОБРАТЬСЯ В КОДЕ(для завершения недели использовал чужой код)
# a = float(input())
# b = float(input())
# c = float(input())
# discriminant = b**2 - 4 * a * c
# x1 = (-b + discriminant ** 0.5) / (2 * a)
# x2 = (-b - discriminant ** 0.5) / (2 * a)
# if x1 and x2 > discriminant:
#     if x1 < x2:
#         print(x1, x2)
#     else:
#         print(x2, x1)
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print(int(x))
# else:
#     print(" ")

#
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2 - 4 * a * c
# if d >= 0:
#     x1 = ((-1 * b) + (d ** 0.5)) / (2 * a)
#     x2 = ((-1 * b) - (d ** 0.5)) / (2 * a)
#     if x1 > x2:
#         print(x2, x1, sep=' ')
#     elif x1 < x2:
#         print(x1, x2, sep=' ')
#     elif x1 == x2:
#         print(x1)


#=======


# from math import *
#
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2 - 4 * a * c
# if d > 0:
#     x1 = (- b - sqrt(d)) / (2 * a)
#     x2 = (- b + sqrt(d)) / (2 * a)
#     if x1 > x2:
#         print(x2, x1)
#     else:
#         print(x1, x2)
# elif d == 0:
#     x1 = (- b + sqrt(d)) / (2 * a)
#     print(x1)

#=======

