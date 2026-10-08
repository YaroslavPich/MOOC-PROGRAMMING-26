text = input("Please type in a word: ")
letter = input("Please type in a character: ")
index = text.find(letter)
if index < len(text) - 3:
    print(text[index:index+3])
