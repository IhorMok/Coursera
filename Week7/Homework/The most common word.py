fin = open('input.txt')
word_dict = {}
for i in fin:
    line = input().split()
    for word in line:
        word_dict[word] = word_dict.get(word, 0) + 1
max_word = max(word_dict.values())
most_frequent = [k for k, v in word_dict.items() if v == max_word]
print(min(most_frequent))
