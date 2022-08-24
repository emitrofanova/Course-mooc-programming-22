# Write your solution here
word = input("Word: ")
print("*" * 30)
if len(word) % 2 == 0:
    print("*" + " " * (14 - len(word)//2) + word + " " * (14 - len(word)//2) + "*")
else:
    print("*" + " " * (13 - len(word)//2) + word + " " * (14 - len(word)//2) + "*")
print("*" * 30)
