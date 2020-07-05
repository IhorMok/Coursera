import math
a = float(input())
b = float(input())
c = float(input())
if a != 0:
    d = b ** 2 - (4 * a * c)
    if d == 0:
        x = -b / (2 * a)
        print((x))
    elif d > 0:
        x1 = float(((-b) + math.sqrt(d)) / (2 * a))
        x2 = float(((-b) - math.sqrt(d)) / (2 * a))
        k1 = x1.is_integer()
        k2 = x2.is_integer()
        if k1 is True and k2 is False:
            if x1 > x2:
                print('{0:.6f}'.format(x2), x1)
            else:
                print(x1, '{0:.6f}'.format(x2))
        elif k1 is False and k2 is True:
            if x2 > x1:
                print('{0:.6f}'.format(x1), x2)
            else:
                print(x2, '{0:.6f}'.format(x1))
        elif k1 is False and k2 is False:
            if x1 > x2:
                print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
            else:
                print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
        else:
            if x1 > x2:
                print(int(x2), int(x1))
            else:
                print(int(x1), int(x2))
