year = int(input("Year: "))
year_new = year
while True:
    year_new += 1
    if year_new % 400 == 0:
        print(f"The next leap year after {year} is {year_new}")
        break
    elif year_new % 4 == 0 and not(year_new % 100 == 0):
        print(f"The next leap year after {year} is {year_new}")
        break
