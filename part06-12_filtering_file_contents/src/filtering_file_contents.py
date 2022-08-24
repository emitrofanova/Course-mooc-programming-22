# Write your solution here
def filter_solutions():
    with open("correct.csv", "w") as f_cor:
        pass
    with open("incorrect.csv", "w") as f_incor:
        pass
    with open("solutions.csv") as f:
        for line in f:
            line_save = line
            line = line.split(";")
            task = []
            if "-" in line[1]:
                task = line[1].split("-")
                answ = int(task[0]) - int(task[1])
            else:
                task = line[1].split("+")
                answ = int(task[0]) + int(task[1])
            if answ == int(line[2]):
                with open("correct.csv", "a") as f_cor:
                    f_cor.write(line_save)
            else:
                with open("incorrect.csv", "a") as f_incor:
                    f_incor.write(line_save)

if __name__ == "__main__":
    filter_solutions()
