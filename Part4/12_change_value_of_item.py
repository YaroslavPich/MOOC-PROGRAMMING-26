first_list = [1, 2, 3, 4, 5]
index_el = 0
new_elem = 0
while True:
    index_el = int(input("Index: "))
    if index_el == -1:
        break
    new_elem = int(input("New value: "))    
    first_list[index_el] = new_elem 
    print(first_list)