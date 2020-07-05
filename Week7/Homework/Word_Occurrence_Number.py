fin = open('input.txt', encoding='utf8')
word_list = {}
for word in fin.read().split():
    word_list[word] = word_list.get(word, 0) + 1
    print(word_list[word] - 1, end=" ")
