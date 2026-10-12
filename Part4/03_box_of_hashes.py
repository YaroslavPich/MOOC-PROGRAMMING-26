def line(times, text):
    if text == "":
        print('*'*times)
    else:
        print(text[0]*times)

def box_of_hashes(height):
    while height != 0:
        line(10, "#")
        height -= 1


if __name__ == "__main__":
    box_of_hashes(5)
