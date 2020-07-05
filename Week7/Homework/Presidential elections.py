fin = open('input.txt', encoding='utf-8')
presindentDict = {}
votes = 0
for line in fin:
    candidate = line.strip()
    presindentDict[candidate] = presindentDict.get(candidate, 0) + 1
    votes += 1
first = max(presindentDict, key=presindentDict.get)
second = open('output.txt', 'w', encoding='utf-8')
if 2 * presindentDict[first] > votes:
    print(first, file=second)
else:
    print(first, file=second)
    print(sorted(presindentDict, key=presindentDict.get, reverse=True)[1],
          file=second)
