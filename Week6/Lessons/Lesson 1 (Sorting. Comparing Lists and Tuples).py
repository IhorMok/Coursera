# a = [3, 1, 2]
# a.sort()
# print(*a)
#=======
# a = [3, 1, 2]
# b = sorted(a, reverse=True) #Создаёт отсортированую копию, не изменяя исходный список
# print(*b)
#======
# print((1, 2) < (1, 'abc'))
#==========
# p = [(172, "Vasya"),
#      (180, "Petya"),
#      (172, "Fedya")]
# p.sort()
# print(*p)
#==========
# p = [(-172, "Vasya"),
#      (-180, "Petya"),
#      (-172, "Fedya")]

# p.sort() #1-ий способ
# for i in range(len(p)):
#     p[i] = (-p[i][0], p[i][1])
# print(*p)
#========
# ls = ['abcd', 'bc', '1234']
# ls.sort(key=len)
# print(*ls)
#======
# points = [
#     (1, 1),
#     (10, 1),
#     (5, 5)
# ]
# def sqrDist(point):
#     return point[0]**2 + point[1]**2
# points.sort(key=sqrDist)
# print(*points)

#=============
# p = [(172, "Vasya"),
#      (180, "Petya"),
#      (172, "Fedya")]
# def makeTuple(man):  #2-й способ
#     return (-man[0], man[1])
# p.sort(key=makeTuple)
# print(*p)
