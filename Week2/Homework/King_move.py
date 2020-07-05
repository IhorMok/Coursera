x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == x2 + 1 or x1 == x2-1 or x1 == x2) and \
        (y1 == y2 + 1 or y1 == y2 - 1 or y1 == y2):
    print("YES")
else:
    print("NO")



a = int(input())
b = int(input())
c = int(input())
if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
    print("rectangular")
elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
    print("obtuse")
elif (a*a + b*b > c*c) or (a*a + c*c > b*b) or (c*c + b*b > a*a):
    print("acute")
else:
    print("impossible")
