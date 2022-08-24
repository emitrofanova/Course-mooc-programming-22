# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        w_fin = input("The word in Finnish: ")
        w_eng = input("The word in English: ")
        with open("dictionary.txt", "a") as f:
            f.write(f"{w_fin} - {w_eng}\n")
        print("Dictionary entry added")
    if function == 2:
        term = input("Search term: ")
        with open("dictionary.txt") as f:
            for line in f:
                line = line.replace("\n", "")
                line_save = line
                line = line.split(" - ")
                if term in line[0] or term in line[1]:
                    print(line_save)
    if function == 3:
        print("Bye!")
        break
