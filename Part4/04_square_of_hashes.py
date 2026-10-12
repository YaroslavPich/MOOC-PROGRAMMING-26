def line(times, text):
    if text == "":
        print('*'*times)
    else:
        print(text[0]*times)

def square_of_hashes(size):
    size_row = size
    while size != 0:
        line(size_row, "#")
        size -= 1


if __name__ == "__main__":
    square_of_hashes(3)
