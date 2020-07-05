# myList = map(int, input().split())
# mySet = set(myList)
# print(mySet)
#======
# mySet = {1, 3.14, 'abc', frozenset((1, 2))}
# print(mySet)
#===
# mySet = {1, 2, 3, 1, 4, 5454543, 4343543,4354}
# print(sorted(list(mySet)))
#=====
# mySet = set('anvcnc')
# print(len(mySet))

#======================LESSONS=============
# mySet = {1, 2, 3, 400000}
# for elem in mySet:
#     print(elem)

#=========
# primes = {2, 3, 5, 7, 11, 13}
# n = int(input())
# if n not in primes:
#     print("not in set")
# else:
#     print("in set")

#=====
# primes = {2, 3, 5, 7, 11, 13}
# primes.add(17)
# print(primes)
# primes.remove(99)
# print(primes)
# primes.discard(99)
# print(primes)

#=====
# a = {1, 2, 3, 4}
# b = {1, 2, 3, 4}
# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)

#=======
# a = {1, 2, 3, 4}
# b = {1, 3, 5}
# print(a ^ b)