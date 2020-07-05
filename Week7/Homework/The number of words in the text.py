import sys
my_set = set()
lines = [line for line in sys.stdin.read().split()]
for word in lines:
    my_set.add(word)
print(len(my_set))
