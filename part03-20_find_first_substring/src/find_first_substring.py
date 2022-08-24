# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
if index + 3 < len(word):
    print(word[index:index + 3])
