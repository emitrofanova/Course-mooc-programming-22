# Write your solution here
import urllib.request
import json

def retrieve_all():
    answ = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    data_correct = json.loads(data)
    for line in data_correct:
        if line["enabled"]:
            answ.append((line["fullName"], line["name"], line["year"], sum(line["exercises"])))
    return answ

def retrieve_course(course_name: str):
    course = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    data_course = course.read()
    data_course_correct = json.loads(data_course)
    answ_dct = {}
    students = 0
    hours = 0
    exer = 0
    for line in data_course_correct:
        if data_course_correct[line]["students"] > students:
            students = data_course_correct[line]["students"]
        hours += data_course_correct[line]["hour_total"] 
        exer += data_course_correct[line]["exercise_total"]
    answ_dct["weeks"] = len(data_course_correct)
    answ_dct["students"] = students
    answ_dct["hours"] = hours
    answ_dct["hours_average"] = hours // students
    answ_dct["exercises"] = exer
    answ_dct["exercises_average"] = exer // students
    return answ_dct

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))
