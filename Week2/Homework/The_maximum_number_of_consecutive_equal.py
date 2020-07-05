n = int(input())
count = 1
max1 = 0
while n != 0:
    n2 = int(input())
    if n2 != n and count > max1:
        max1 = count
        count = 1
    elif n2 != n:
        count = 1
    else:
        count += 1
    n = n2
print(max1)
