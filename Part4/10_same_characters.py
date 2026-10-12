def same_chars(text, first, second):
    if first > second or first > len(text) - 1 or second > len(text) - 1:
        return False
    if text[first] == text[second]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
