# Write your solution here
story = ""
prev = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == prev:
        print(story)
        break
    else:
        story += word + " "
    prev = word

