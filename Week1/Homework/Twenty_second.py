n1 = int(input())
n2 = int(input())
a = 0 ** (n1 % n2)
b = 1 - 0 ** (n1 % n2)
print("YES" * a, "NO" * b, sep="")
# print(-7%3)