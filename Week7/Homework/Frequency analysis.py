with open("input.txt", "r", encoding="UTF8") as input_file:
    words = {}
    for line in input_file:
        for word in line.split():
            words[word] = words.get(word, 0) + 1
wordsList = [(-value, key) for key, value in words.items()]
wordsList.sort()
for word in wordsList:
    print(word[1])
