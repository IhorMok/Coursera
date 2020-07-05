# Сюда идёт файл input.txt
# fin = open('input.txt', 'r', encoding='utf8')
# a = int(fin.readline())
# b = int(fin.readline())
# print(a + b)
#======
fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
print([lines[0].strip(), lines[1].strip()])
#=============
# fin = open('input.txt', 'r', encoding='utf8')
# for line in fin:
#     print(int(line))
#========
# fin = open('input.txt', 'r', encoding='utf8')
# s = fin.read()
# print([s])
#=======
# fout = open('output.txt', 'w', encoding='utf8')
# print(sum(map(int, fin.readlines())), file=fout)
# fout.close()
