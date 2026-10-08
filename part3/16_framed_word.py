word = input("Word: ")
output = (26-len(word))//2+1
left = 27 - output - len(word)
print("*"*30)
print(f"*{output*' '}{word}{left*' '} *")
print("*"*30)
