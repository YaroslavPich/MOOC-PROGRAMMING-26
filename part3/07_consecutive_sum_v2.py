limit = int(input("Limit: "))
number = 1
suma = 1
string = str(number)

while suma < limit:
    number += 1
    suma += number
    if number != 1:
        string += ' + ' + str(number)    
    
print(f"The consecutive sum: {string} = {suma}")
