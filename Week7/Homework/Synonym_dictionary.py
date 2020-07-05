n = int(input())
myDict = {}
for word in range(n):
    first, second = input().split()
    myDict[first] = second
    myDict[second] = first
print(myDict[input()])
