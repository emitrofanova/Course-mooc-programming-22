# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth = datetime(year, month, day)
new_millennium = datetime(1999, 12, 31) 

if birth < new_millennium:
    print(f"You were {(new_millennium - birth).days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
