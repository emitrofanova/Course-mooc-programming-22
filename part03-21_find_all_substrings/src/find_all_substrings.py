# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = 1
while index >= 0 and len(word) > 2:
    index = word.find(character)
    if index + 3 <= len(word):
        print(word[index:index + 3])
    word = word[index + 1:]
