# Write your solution here:
class CourseList:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course: str, grade: int, credit: int):
        if not course in self.__courses:
            self.__courses[course] = [0, 0]
        if grade > self.__courses[course][0]:
            self.__courses[course][0] = grade
        self.__courses[course][1] = credit

    def get_data(self, course: str):
        if not course in self.__courses:
            return None
        return self.__courses[course]

    def all_data(self):
        return self.__courses

class CourseListApplication:
    def __init__(self):
        self.__courselist = CourseList()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__courselist.add_course(course, grade, credit)

    def get_course_data(self):
        course = input("course: ")
        course_data = self.__courselist.get_data(course)
        if course_data == None:
            print("no entry for this course")
        else:
            print(f"{course} ({course_data[1]} cr) grade {course_data[0]}")

    def statistics(self):
        courses_data = self.__courselist.all_data()
        total = 0
        dct_grades = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        sum_grades = 0
        for course in courses_data:
            total += courses_data[course][1]
            dct_grades[courses_data[course][0]] += 1
            sum_grades += courses_data[course][0]
        print(f"{len(courses_data)} completed courses, a total of {total} credits")
        print(f"mean {(sum_grades / len(courses_data)):.1f}")
        print("grade distribution")
        for i in [5, 4, 3, 2, 1]:
            print(f"{i}: ", end="")
            for j in range(dct_grades[i]):
                print("x", end="")
            print()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

# when testing, no code should be outside application except the following:
application = CourseListApplication()
application.execute()
