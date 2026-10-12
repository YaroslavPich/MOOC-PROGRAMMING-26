def line(size, character):
    count = 1
    while count <= size:
        print(count * character)
        count += 1

def triangle(size):
    line(size, "#")


if __name__ == "__main__":
    triangle(5)
