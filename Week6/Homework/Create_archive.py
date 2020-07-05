disk_space, n = list(map(int, input().split()))
data_size = []
for i in range(n):
    data_size.append(int(input()))
data_size.sort()
count_people = 0
summa = 0
for elements in range(len(data_size)):
    if summa + data_size[elements] <= disk_space:
        summa += data_size[elements]
        count_people = count_people + 1
print(count_people)
