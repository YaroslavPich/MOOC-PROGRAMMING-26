text = input("Please type in a sentence: ")
i = 0
print(text[0])
while i< len(text):
    if text[i] != len(text) and text[i] == " ":
        print(text[i+1])
    i += 1