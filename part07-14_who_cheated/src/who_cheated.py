# Write your solution here
import csv
from datetime import datetime

def cheaters():
    dct_students = {}
    answ = []
    with open("start_times.csv") as f1:
        for line in csv.reader(f1, delimiter=";"):
            dct_students[line[0]] = [line[1]]
    with open("submissions.csv") as f2:
        for line in csv.reader(f2, delimiter=";"):
            if len(dct_students[line[0]]) == 1:
                dct_students[line[0]].append(line[3])
            elif line[3] > dct_students[line[0]][1]:
                dct_students[line[0]][1] = line[3]
    for student in dct_students:
        start = dct_students[student][0].split(":")
        finish = dct_students[student][1].split(":")
        delta = datetime(1, 1, 1, int(finish[0]), int(finish[1])) - datetime(1, 1, 1, int(start[0]), int(start[1]))
        if delta.seconds > 10800:
            answ.append(student)
    return answ

if __name__ == "__main__":
    print(cheaters())
