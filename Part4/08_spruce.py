def spruce(times):
    print("a spruce!")
    count_line = 1
    count = 1
    amoung = times - 1
    while count_line <= times:
        print(f'{amoung*" "}{count*"*"}')
        amoung -= 1
        count += 2
        count_line += 1
    print(f'{(times-1)*" "}*')


if __name__ == "__main__":
    spruce(5)
