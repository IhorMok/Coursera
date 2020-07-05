s = input()
a = s.find('f')
if a == -1:
    print("-2")
else:
    print(s.find('f', a+1))
