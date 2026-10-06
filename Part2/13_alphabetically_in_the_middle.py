letter1 = input("1st letter: ")
letter2 = input("2st letter: ")
letter3 = input("3st letter: ")

if letter1 > letter2 and letter1 > letter3 and letter2 > letter3:
    print(f"The letter in the middle is {letter2}")
if letter3 > letter2 and letter3 > letter1 and letter2 > letter1:
    print(f"The letter in the middle is {letter2}") 
if letter2 > letter1 and letter2 > letter3 and letter1 > letter3:
    print(f"The letter in the middle is {letter1}")
if letter3 > letter1 and letter3 > letter2 and letter1 > letter2:
    print(f"The letter in the middle is {letter1}") 
if letter2 > letter1 and letter2 > letter3 and letter3 > letter1:
    print(f"The letter in the middle is {letter3}")
if letter1 > letter3 and letter1 > letter2 and letter3 > letter2:
    print(f"The letter in the middle is {letter3}") 
