# Write your solution here
line = input("Please type in a sentence: ")
print(line[0])
i = 0
while i < len(line):
    if line[i] == " ":
        print(line[i + 1])
    i += 1
