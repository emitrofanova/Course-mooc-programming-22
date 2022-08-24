# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name in students:
        if students[name] == []:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(students[name])} completed courses:")
            sum_marks = 0
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
                sum_marks += course[1]
            print(f" average grade {sum_marks/len(students[name])}")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    flag = True
    if course[1] != 0:
        for i in students[name]:
            if course[0] == i[0]:
                flag = False
                if course[1] > i[1]:
                    students[name].remove((course[0], i[1]))
                    students[name].append(course)
    if flag and course[1] != 0:
        students[name].append(course)

def summary(students: dict):
    max_courses = 0
    max_aver = 0
    for student in students:
        sum_marks = 0
        aver = 0
        if len(students[student]) > max_courses:
            max_courses = len(students[student])
            name_max_courses = student
        for course in students[student]:
            sum_marks += course[1]
            aver = sum_marks/len(students[student])
        if aver > max_aver:
            max_aver = aver
            name_max_aver = student
    print(f"students {len(students)}")   
    print(f"most courses completed {max_courses} {name_max_courses}")
    print(f"best average grade {max_aver} {name_max_aver}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
