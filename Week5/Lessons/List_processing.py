# a = list(map(int, input().split()))
# i = 0
# while i < len(a):
#     if a[i] % 2 != 0:
#         a.pop(i)
#     else:
#         i += 1
# print(*a)

# for i in range(len(a)):
#     if a[i] % 2 != 0:
#         a.pop(i)
# print(*a)

#============

a = list(map(int, input().split()))
b = []
for now in a:
    if now % 2 == 0:
        b.append(now)
print(*b)