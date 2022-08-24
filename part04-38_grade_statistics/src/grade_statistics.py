# Write your solution here

def inp():
    #input from user
    all = []
    while True:
        student = input("Exam points and exercises completed: ").split()
        if student == []:
            break
        all.append(student)
    return all

def aver(all_list):
    #points average
    cnt = 0
    for i in all_list:
        cnt += int(i[0]) + (int(i[1]) // 10)
    return f"{cnt / len(all_list):.1f}"
    
def perc(all_list):
    #pass percentage
    cnt = 0
    for i in all_list:
        if int(i[0]) >= 10 and (int(i[0]) + int(i[1]) // 10) >= 15:
            cnt += 1
    return f"{cnt / len(all_list) * 100:.1f}"

def grades(all_list):
    grades = [0, 0, 0, 0, 0, 0]
    for j in all_list:
        if (int(j[0]) < 10) or (int(j[0]) + int(j[1]) // 10) <= 14:
            grades[0] += 1
        elif 15 <= int(j[0]) + int(j[1]) // 10 <= 17:
            grades[1] += 1
        elif 18 <= int(j[0]) + int(j[1]) // 10 <= 20:
            grades[2] += 1
        elif 21 <= int(j[0]) + int(j[1]) // 10 <= 23:
            grades[3] += 1
        elif 24 <= int(j[0]) + int(j[1]) // 10 <= 27:
            grades[4] += 1
        elif 28 <= int(j[0]) + int(j[1]) // 10 <= 30:
            grades[5] += 1
    return grades

def print_answ(aver, perc, grades, all_list):
    #print statistics and grade distribution
    print("Statistics:")
    print("Points average:", aver)
    print("Pass percentage:", perc)
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: ", end="")
        print("*" * grades[i])

def main():
    all_students = inp()
    average = aver(all_students)
    percentage = perc(all_students)
    grade = grades(all_students)
    print_answ(average, percentage, grade, all_students)

main()
