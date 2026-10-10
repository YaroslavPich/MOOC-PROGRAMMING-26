# Write your solution here
def hash_square(time):
    i = time
    while time > 0:
        print(i*"#")
        time -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)