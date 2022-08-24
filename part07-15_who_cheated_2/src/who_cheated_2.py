# Write your solution here
import csv
from datetime import datetime

def final_points():
    dct_students = {}
    answ = {}
    with open("start_times.csv") as f1:
        for line in csv.reader(f1, delimiter=";"):
            dct_students[line[0]] = [line[1]]
    with open("submissions.csv") as f2:
        for line in csv.reader(f2, delimiter=";"):
            if len(dct_students[line[0]]) == 1:
                dct_students[line[0]].append({})
            start = dct_students[line[0]][0].split(":")
            finish = line[3].split(":")
            delta = datetime(1, 1, 1, int(finish[0]), int(finish[1])) - datetime(1, 1, 1, int(start[0]), int(start[1]))
            if delta.seconds <= 10800:
                if line[1] not in dct_students[line[0]][1]:
                    dct_students[line[0]][1][line[1]] = 0
                if int(line[2]) > dct_students[line[0]][1][line[1]]:
                    dct_students[line[0]][1][line[1]] = int(line[2]) 
    for student in dct_students:
        total_points = 0
        for exer in dct_students[student][1]:
            total_points += dct_students[student][1][exer]
        answ[student] = total_points
    return answ

if __name__ == "__main__":
    print(final_points())
