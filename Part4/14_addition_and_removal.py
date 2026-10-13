print("The list is now []")
list_mod = []
choise = ""
i = 1
while choise != "x":
    choise = input("a(d)d, (r)emove or e(x)it: d")
    if choise == "d":
        list_mod.append(i)
        i += 1
        print(f"The list is now {list_mod}")
    elif choise == "r":
        list_mod.pop()
        i -= 1
        print(f"The list is now {list_mod}")
    elif choise == "x":
        print("Bye!")
        break
