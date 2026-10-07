string_input = input("Please type in a string: ")
i = 1
while i <= len(string_input):
    print(string_input[len(string_input)-(len(string_input)+i)])
    i += 1
