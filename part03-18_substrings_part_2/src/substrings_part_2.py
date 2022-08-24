# Write your solution here
word = input("Please type in a string: ")
i = -1
while i + 1 > - len(word):
    print(word[i:])
    i -= 1