file_score = open('input.txt', 'r', encoding='utf8')
k = int(file_score.readline())
bound = 40
abiturs = []
for line in file_score:
    line_split = line.split()
    condition = (int(line_split[-1]) >= bound) and \
                (int(line_split[-2]) >= bound) and \
                (int(line_split[-3]) >= bound)
    if condition:
        summMarks = int(line_split[-3]) + \
                    int(line_split[-2]) + \
                    int(line_split[-1])
        abiturs.append(summMarks)
abiturs.sort(reverse=True)
if len(abiturs) == 0:
    print(1)
elif len(abiturs) <= k:
    print(0)
elif abiturs[0] == abiturs[k]:
    print(1)
else:
    counter = 1
    enterMark = abiturs[0]
    while counter <= k:
        if abiturs[counter] < abiturs[counter - 1]:
            enterMark = abiturs[counter - 1]
        counter += 1
    print(enterMark)
