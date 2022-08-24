# Write your solution here
def filter_incorrect():
    with open("correct_numbers.csv", "w") as f_answ:
        pass
    with open("lottery_numbers.csv") as f:
        for line in f:
            line_save = line
            line = line.replace("\n", "")
            line = line.split(";")
            week = line[0].split()
            numbers = line[1].split(",")
            Flag = True
            for num in numbers:
                try:
                    if int(num) > 39 or int(num) < 1:
                        Flag = False
                except ValueError:
                    Flag = False
            try:
                week[1] = int(week[1])
            except ValueError:
                    Flag = False
            if len(numbers) != 7 or len(set(numbers)) != len(numbers):
                Flag = False
            if Flag:
                with open("correct_numbers.csv", "a") as f_answ:
                    f_answ.write(line_save)

if __name__ == "__main__":
    filter_incorrect()

