s = input()
one = s.find('f')
two = s.rfind('f')
if one == -1:
    print()
elif one == two:
    print(one)
else:
    print(one, two)
