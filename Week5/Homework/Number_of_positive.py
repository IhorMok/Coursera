positive = input().split()
n = 0
for i in positive:
    if int(i) > 0:
        n = n + 1
print(n, end=" ")
