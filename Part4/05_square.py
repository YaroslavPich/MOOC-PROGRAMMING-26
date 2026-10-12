def line(times, text):
    print(text*times)

def square(size, character):
    count = size
    while count != 0:
        line(size, character)
        count -= 1


if __name__ == "__main__":
    square(5, "0")
