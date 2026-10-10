number = int(input("Please type in a number: "))
i = 1
j = number
while i < j:
    print(i)
    print(j)
    i+=1
    j-=1
if number % 2 == 1:
    print(i)