def line(times, text):
    if text == "":
        print('*'*times)
    else:
        print(text[0]*times)


if __name__ == "__main__":
    line(5, "x")
