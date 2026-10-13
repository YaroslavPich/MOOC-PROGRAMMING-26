second_list = []
quantity_items = int(input('How many items: '))
element = 0
for i in range(quantity_items):
    element = int(input(f'Item {i+1}: '))
    second_list.append(element)
print(second_list)
