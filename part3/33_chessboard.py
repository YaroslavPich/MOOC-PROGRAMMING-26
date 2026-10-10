# Write your solution here
def chessboard(box):
    row = box
    i = 1
    while box > 0:
        count = row
        while count > 0:
            if (count+box) % 2 == 0:
                print(1, end='')
            else:
                print(0, end='')           
            count -= 1
        print()
        box -=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
