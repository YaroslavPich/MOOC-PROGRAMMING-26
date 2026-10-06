attemp = 0
while True:
    attemp += 1
    pin = input("PIN: ")
    if pin == '4321':
        break
    print("Wrong")
if attemp == 1:
    print('Correct! It only took you one single attempt!')
else:
    print(f"Correct! It took you {attemp} attempts")
