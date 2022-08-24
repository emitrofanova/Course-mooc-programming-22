# wwite your solution here

# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

with open(student_info) as students:
    dct_students = {}
    for line in students:
        line = line.strip()
        line = line.split(";")
        if line[0] == "id":
            continue
        dct_students[line[0]] = line[1] + " " + line[2]

with open(exercise_data) as exercises:
    dct_exercises = {}
    for line in exercises:
        line = line.split(";")
        sum_num = 0
        if line[0] == "id":
            continue
        for num in line[1:]:
            sum_num += int(num)
        if sum_num // 4 >= 10:
            dct_exercises[line[0]] = 10
        else:
            dct_exercises[line[0]] = sum_num // 4
            
with open(exam_points) as exam:
    dct_grade = {}
    for line in exam:
        sum_num = 0
        line = line.split(";")
        if line[0] == "id":
            continue
        for num in line[1:]:
            sum_num += int(num)
        dct_grade[line[0]] = sum_num

for key in dct_students:
    if key in dct_exercises and key in dct_grade:
        final_grade = dct_exercises[key] + dct_grade[key]
        if final_grade <= 14:
            print(dct_students[key], 0)
        if final_grade >= 15 and final_grade < 18:
            print(dct_students[key], 1)
        if final_grade >= 18 and final_grade < 21:
            print(dct_students[key], 2)
        if final_grade >= 21 and final_grade < 24:
            print(dct_students[key], 3)
        if final_grade >= 24 and final_grade < 28:
            print(dct_students[key], 4)
        if final_grade >= 28:
            print(dct_students[key], 5)
