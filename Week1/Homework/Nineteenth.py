# Улитка
h = int(input())
a = int(input())
b = int(input())
step = a - b
dist = h - a
print(((dist + step - 1) // step) + 1)
