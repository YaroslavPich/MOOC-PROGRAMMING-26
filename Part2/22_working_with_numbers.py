print("Please type in integer numbers. Type in 0 to finish.")
count = 0
suma = 0
positive = 0
negative = 0
mean = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count +=1
    suma += number
    mean = suma / count
    if number > 0:
        positive += 1
    else:
        negative += 1
print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
