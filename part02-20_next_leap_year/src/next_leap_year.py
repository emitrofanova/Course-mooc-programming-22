# Write your solution here
year = int(input("Year: "))
year_leap = year
while True:
    year_leap += 1
    if (year_leap % 4 == 0 and year_leap % 100 == 0 and year_leap % 400 == 0) or (year_leap % 4 == 0 and not(year_leap % 100 == 0)):
        print(f"The next leap year after {year} is {year_leap}")
        break


