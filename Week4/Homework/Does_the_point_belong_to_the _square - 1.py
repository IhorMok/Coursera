def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1)


x = float(input())
y = float(input())
print("YES" * IsPointInSquare(x, y), "NO" * (IsPointInSquare(x, y) - 1) ** 2)
