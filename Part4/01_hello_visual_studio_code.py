while True:
    course = input("Editor: ").lower()
    if course in ['word', 'notepad']:
        print("awful")
    elif course != "visual studio code":
        print("not good")
    else:
        print("an excellent choice!")
        break
