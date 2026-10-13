def first_word(sentence):
    first = ""
    for i in sentence:
        if i != ' ':
            first += i
        else:
            break
    return first

def second_word(sentence):
    sentence = sentence[len(first_word(sentence))+1:]
    return first_word(sentence)

def last_word(sentence):
    i = -1
    index = 0
    while sentence[i] != " ":
        index = i
        i -= 1
    return sentence[index:]


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
