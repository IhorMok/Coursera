my_number = [int(s) for s in input().split()]
occur_before = set()
for n in my_number:
    if n in occur_before:
        print("YES")
    else:
        print("NO")
        occur_before.add(n)
