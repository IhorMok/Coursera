# a = 1
# b = 2
# a, b = b, a
# print(a, b)

#=====
# a, b, c = 1, 2, 3
# a, b, c = c, b, a
# print(a, b, c)

#====
# myRange = range(10)
# print(tuple(myRange))

#=====
# print(tuple("abvdsd"))

#========
# for color in ("red", 'green', 'yellow'):
#     print(color, 'apple')

#====
# for i in range(25):
#     print(i)

#===
# for i in range(10, -1, -1):
#     print(i, end=' ')
#===
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
