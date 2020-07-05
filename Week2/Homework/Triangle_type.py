a = int(input())
b = int(input())
c = int(input())
if a < (b + c) or b < (a + c) or c < (a + b):
    if a ** 2 + b ** 2 == c ** 2:
        print('rectangular')
    elif b ** 2 + c ** 2 == a ** 2:
        print('rectangular')
    elif a ** 2 + c ** 2 == b ** 2:
        print('rectangular')
    elif a ** 2 + b ** 2 < c ** 2:
        print('obtuse')
    elif b ** 2 + c ** 2 < a ** 2:
        print('obtuse')
    elif a ** 2 + c ** 2 < b ** 2:
        print('obtuse')
    elif a ** 2 + b ** 2 > c ** 2:
        print('abuse')
    elif b ** 2 + c ** 2 > a ** 2:
        print('abuse')
    elif a ** 2 + c ** 2 > b ** 2:
        print('abuse')
else:
    print('impossible')
