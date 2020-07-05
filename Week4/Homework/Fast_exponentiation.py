b = float(input())
n = float(input())


def rec(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return rec(b*b, n/2)
    else:
        return b*rec(b, n-1)
print(rec(b, n))
