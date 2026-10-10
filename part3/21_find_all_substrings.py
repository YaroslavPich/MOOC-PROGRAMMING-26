text = input("Please type in a word: ")
letter = input("Please type in a character: ")
while len(text) >= 3:
    index = text.find(letter)
    if index != -1 and index <= len(text) - 3:
        print(text[index:index+3])
    else:
        break
    text = text[index+1:]