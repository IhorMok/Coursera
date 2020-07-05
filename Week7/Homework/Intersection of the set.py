first_list = set(map(int, input().split()))
second_list = set(map(int, input().split()))
intersection = first_list & second_list
print(*sorted(intersection))
