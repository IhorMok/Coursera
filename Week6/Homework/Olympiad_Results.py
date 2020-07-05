n = int(input())
resultList = []
for i in range(n):
    k = list(input().split())
    resultList.append(k)
print(resultList)
resultList.sort(key=lambda x: int(x[1]), reverse=True)
print(resultList)
for i in resultList:
    print(i[0])
