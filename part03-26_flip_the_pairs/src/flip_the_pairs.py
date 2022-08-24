# Write your solution here
num = int(input("Please type in a number: "))
i = 1
while i <= num:
    if i % 2 == 1:
        if i + 1 <= num:
            print(i + 1)
        else:
            print(i)
    else:
        print(i - 1)
    i += 1
