list_word = []
word = input("Word: ")
list_word.append(word)
i = 1
while True:
    word_next = input("Word: ")
    if word_next not in list_word:
        list_word.append(word_next)
        i += 1
    else:
        break
print(f"You typed in {i} different words")
