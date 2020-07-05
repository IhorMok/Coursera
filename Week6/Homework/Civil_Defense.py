n = int(input()) # Разобраться
s = list(map(int, input().split()))
for j in range(n):
    s[j] = [s[j], j]
m = int(input())
b = list(map(int, input().split()))
for j in range(m):
    b[j] = [b[j], j]
s.sort()
b.sort()
r = list()
j = 0
start = 0
for i in range(n):
    min = abs(s[i][0] - b[0][0])
    index = 0
    for j in range(start, m):
        if abs(s[i][0] - b[j][0]) <= min:
            min = abs(s[i][0] - b[j][0])
            index = b[j][1]
        else:
            start = j - 1
            break
    r.append((s[i][1], index + 1))
r.sort()
for i in range(len(r)):
    print(r[i][1], end=' ')
