# Write your solution here
num = int(input("Please type in a number: "))
i = 1
j = - 1
if num % 2 == 0:
    while i <= num // 2:
        print(i)
        i += 1
        j += 1
        print(num - j)
else:
    while i <= num // 2:
        print(i)
        i += 1
        j += 1
        print(num - j)
    print(num // 2 + 1)

