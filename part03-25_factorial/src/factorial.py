# Write your solution here
num = int(input("Please type in a number: "))
while num > 0:
    i = 1
    fact = 1
    while i <= num:
        fact *= i
        i += 1
    print(f"The factorial of the number {num} is {fact}")
    num = int(input("Please type in a number: "))
print("Thanks and bye!")
