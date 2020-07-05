file_input = open("input.txt", 'r', encoding='utf-8')
file_output = open('output.txt', 'w', encoding='utf8')
my_list = []
for line in file_input:
    my_list.append(line.split())
my_list.sort()
file_input.close()
for i in range(len(my_list)):
    print(*my_list[i][:2], my_list[i][3], file=file_output)
