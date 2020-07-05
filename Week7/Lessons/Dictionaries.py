# capitals = {"Russia": "Moscow", "France": "Paris"}
# capitals["USA"] = "Washington"
# print(capitals)
# del capitals["France"]
# print(capitals)
# print('Russia' in capitals)
#=========
# myDict = dict([("x", 5), ('y', 3)])
# for i in myDict:
#     print(i, myDict[i])

#=============VER_1
# s = input()
# letters = dict()
# for c in s:
#     if c in letters:
#         letters[c] += 1
#     else:
#         letters[c] = 1
# for c in sorted(letters):
#     print(c, letters[c])
#============VER_2
# s = input()
# letters = dict()
# for c in s:
#     if c not in letters:
#         letters[c] = 0
#     letters[c] += 1
# for c in sorted(letters):
#     print(c, letters[c])
#==============VER_3
# s = input()
# letters = dict()
# for c in s:
#     letters[c] = letters.get(c, 0) + 1
# for c in sorted(letters):
#     print(c, letters[c])

#============ver1
# gasCost = {}
# n = int(input())
# a92, a95, a98 = map(int, input().split())
# gasCost[92] = a92
# gasCost[95] = a95
# gasCost[98] = a98
# for i in range(n - 1):
#     a92, a95, a98 = map(int, input().split())
#     gasCost[92] = min(a92, gasCost[92])
#     gasCost[95] = min(a95, gasCost[95])
#     gasCost[98] = min(a98, gasCost[98])
# print(gasCost[92], gasCost[95], gasCost[98])

#=============ver2
# gasCost = {}
# n = int(input())
# costs = list(map(int, input().split()))
# btypes = (92, 95, 98)
# for now in range(len(btypes)):
#     gasCost[btypes[now]] = costs[now]
# for i in range(n - 1):
#     costs = list(map(int, input().split()))
#     btypes = (92, 95, 98)
#     for now in range(len(btypes)):
#         gasCost[btypes[now]] = min(costs[now], gasCost[btypes[now]])
# print(gasCost[92], gasCost[95], gasCost[98])

#==============
# fin = open('input.txt')
# myDict = {}
# for line in fin:
#     eng, latins = line.split('-')
#     latinsList = latins.split(',')
#     eng = eng.strip()
#     for latin in latinsList:
#         if latin.strip() not in myDict:
#             myDict[latin.strip()] = []
#         myDict[latin.strip()].append(eng)
# for latin in sorted(myDict):
#     print(latin, '-', ', '.join(sorted(myDict[latin])))

#=============
tree = {'a':{
            'b': dict(),
            'c': {
                'd': dict(),
                'e': dict()
             }

        }
    }
print(tree)