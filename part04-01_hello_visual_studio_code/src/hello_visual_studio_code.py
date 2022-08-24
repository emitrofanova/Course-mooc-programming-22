# Write your solution here
editor = input("Editor: ").lower()
while editor != "visual studio code":
    if editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
    editor = input("Editor: ").lower()
print("an excellent choice!")
