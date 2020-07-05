# Симметричное число, правильно
n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 100 % 10
diff1 = (a - d) ** 2
diff2 = (b - c) ** 2
print((diff1 + diff2) + 1)
