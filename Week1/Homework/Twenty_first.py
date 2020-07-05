# Максимум из двух
number1 = int(input())
number2 = int(input())

c = number1 // number2
d = number2 // number1
print((number1 * c + number2 * d) // (c + d))
