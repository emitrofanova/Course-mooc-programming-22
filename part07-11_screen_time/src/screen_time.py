# Write your solution here
from datetime import datetime, timedelta

file_data = input("Filename: ")
starting_date = input("Starting_date: ")
number_days = int(input("How many days: "))
start = starting_date.split(".")
start = datetime(int(start[2]), int(start[1]), int(start[0]))
print("Please type in screen time in minutes on each day (TV computer mobile):")
i = 0
all_days = []
total = 0
aver = 0
while i != number_days:
    days = timedelta(days=i)
    new_day = (start + days).strftime("%d.%m.%Y")
    screen_time = input(f"Screen time {new_day}: ")
    screen_time_list = screen_time.split()
    total += int(screen_time_list[0]) + int(screen_time_list[1]) + int(screen_time_list[2])
    i += 1
    aver = total / i
    all_days.append(f"{new_day}: {screen_time_list[0]}/{screen_time_list[1]}/{screen_time_list[2]}")
with open(file_data, "w") as f:
    start = start.strftime("%d.%m.%Y")
    f.write(f"Time period: {start}-{new_day}\n")
    f.write(f"Total minutes: {total}\n")
    f.write(f"Average minutes: {aver}\n")
    for i in all_days:
        f.write(i)
        f.write("\n")
print("Data stored in file", file_data)
