# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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
        dct_exercises[line[0]] = sum_num

for key in dct_students:
    if key in dct_exercises:
        print(dct_students[key], dct_exercises[key])
