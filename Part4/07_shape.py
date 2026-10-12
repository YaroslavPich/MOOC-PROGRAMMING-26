def line1(size, character):
    count = 1
    while count <= size:
        print(count * character)
        count += 1

def line2(size, times, text):
    count = 1
    while count<= times:
        print(size*text)
        count += 1

def shape(size, character, times, text):
    line1(size, character)
    line2(size, times, text)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
