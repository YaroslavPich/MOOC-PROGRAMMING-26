# Write your solution here
def squared(box, position):
    text = box * position ** 2
    pos = 0
    i = position
    while i > 0:
        print(text[pos:pos+position])
        pos += position
        i-=1


# Testing the function
if __name__ == "__main__":
    squared("ab", 3)