password = input("Password: ")
while True:
    password_repeat = input("Repeat password: ")
    if password != password_repeat:
        print("They do not match!")
    else:
        break
print("User account created!")
