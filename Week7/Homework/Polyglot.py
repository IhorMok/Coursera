n = int(input())
language = []
for _ in range(n):
    k = int(input())
    new_set = set()
    for _ in range(k):
        new_set.add(input())
    language.append(new_set)
unic = set.union(*language)
intersec = set.intersection(*language)
print(len(intersec), '\n'.join(sorted(intersec)), len(unic),
      '\n'.join(sorted(unic)), sep='\n')
