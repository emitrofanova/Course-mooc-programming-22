# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        new_line = input("Diary entry: ")
        with open("diary.txt", "a") as f:
            f.write(new_line + "\n")
        print("Diary saved")
        print()
    if function == 2:
        print("Entries:")
        with open("diary.txt") as f:
            print(f.read())
    if function == 0:
        print("Bye now!")
        break
