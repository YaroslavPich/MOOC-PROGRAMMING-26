list_sort = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    list_sort.append(item)
    list_sort_new = sorted(list_sort)
    print(f"The list now: {list_sort}")
    print(f"The list in order: {list_sort_new}")
