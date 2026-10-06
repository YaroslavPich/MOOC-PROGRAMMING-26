# Write your solution here
sentence = ""
word_double = ""
while True:
    word = input("Please type in a word: ")

    if word == "end" or word == word_double:
        break
    else:
        sentence += word + " "
        word_double = word
print(sentence)
