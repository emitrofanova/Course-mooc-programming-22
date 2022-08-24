# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_inf = input("Course information: ")

with open(student_info) as students:
    dct_students = {}
    for line in students:
        line = line.strip()
        line = line.split(";")
        if line[0] == "id":
            continue
        dct_students[line[0]] = line[1] + " " + line[2]

with open(exercise_data) as exercises:
    dct_grades = {}
    for line in exercises:
        line = line.split(";")
        exec_nbr = 0
        if line[0] == "id":
            continue
        dct_grades[line[0]] = []
        for num in line[1:]:
            exec_nbr += int(num)
        dct_grades[line[0]].append(exec_nbr)
        exec_pts = exec_nbr // 4
        if exec_pts // 4 >= 10:
            dct_grades[line[0]].append(10)
        else:
            dct_grades[line[0]].append(exec_pts) 
            
with open(exam_points) as exam:
    for line in exam:
        exm_pts = 0
        line = line.split(";")
        if line[0] == "id":
            continue
        for num in line[1:]:
            exm_pts += int(num)
        dct_grades[line[0]].append(exm_pts)

for i in dct_grades:
    tot_pts = dct_grades[i][1] + dct_grades[i][2]
    dct_grades[i].append(tot_pts)
    if tot_pts <= 14:
        dct_grades[i].append(0)
    if tot_pts >= 15 and tot_pts < 18:
        dct_grades[i].append(1)
    if tot_pts >= 18 and tot_pts < 21:
        dct_grades[i].append(2)
    if tot_pts >= 21 and tot_pts < 24:
        dct_grades[i].append(3)
    if tot_pts >= 24 and tot_pts < 28:
        dct_grades[i].append(4)
    if tot_pts >= 28:
        dct_grades[i].append(5)

head = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]

with open("results.txt", "w") as f_res_txt:
    with open(course_inf) as f_course_inf:
        text = f_course_inf.read().split("\n")
        f_res_txt.write(f"{text[0][6:]}, {text[1][15:]} credits\n")
        f_res_txt.write("======================================\n")

with open("results.txt", "a") as f_res_txt:
    f_res_txt.write(f"{head[0]:30}{head[1]:10}{head[2]:10}{head[3]:10}{head[4]:10}{head[5]:10}\n")
    for key in dct_students:
        if key in dct_grades:
            f_res_txt.write(f"{dct_students[key]:30}{dct_grades[key][0]:<10}{dct_grades[key][1]:<10}{dct_grades[key][2]:<10}{dct_grades[key][3]:<10}{dct_grades[key][4]:<10}\n")

with open("results.csv", "w") as f_res_csv:
    pass

with open("results.csv", "a") as f_res_csv:
    for key in dct_students:
        if key in dct_grades:
            f_res_csv.write(f"{key};{dct_students[key]};{dct_grades[key][4]}\n")

print("Results written to files results.txt and results.csv")
