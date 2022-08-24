# Write your solution here
first = input("Please type in string 1: ")
second = input("Please type in string 2: ")
if len(first) > len(second):
    print(first, "is longer")
elif len(second) > len(first):
    print(second, "is longer")
else:
    print("The strings are equally long")