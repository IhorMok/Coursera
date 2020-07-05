n = input().split()
for e in range(len(n)):
    n[e] = int(n[e])
for e in range(1, len(n)):
    if n[e] > n[e - 1]:
        print(n[e], end=" ")
