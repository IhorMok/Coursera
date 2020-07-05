# a = list('abcdef')
# a[0] = 'g'
# s = ''.join(a)
# print(s)

#====
# wordList = input().split()
# print(wordList)

#====
intList = list(map(int, input().split()))
#print(" ".join(map(str, intList)))
print(*intList)