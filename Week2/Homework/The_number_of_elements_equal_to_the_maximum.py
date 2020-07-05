n = int(input())
s = 0
m = 1
while n != 0:
    if n > s:
        s = n
        m = 1
    elif n == s:
        m = m + 1
    n = int(input())
print(m)
