text = input("Please type in a string: ")
search = "aeo"
i = 0
while i < len(search):
    find = search[i]
    if find in text:
        print(f"{find} found")
    else:
        print(f"{find} not found")
    i += 1
