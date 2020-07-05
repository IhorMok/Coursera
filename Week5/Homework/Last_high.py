last = input().split()
count_index = 0
count_value = 0
for i, elements in enumerate(last):
    if int(elements) >= int(count_value):
        count_index, count_value = i, elements
print(count_value, count_index)
