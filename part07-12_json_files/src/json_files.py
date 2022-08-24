# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()
    people = json.loads(data)
    for person in people:
        print(person["name"] + " " + str(person["age"]) + " years (", end = "")
        h = []
        for hobby in person["hobbies"]:
            h.append(hobby)
        print(*h, sep = ", ", end = ")\n")

if __name__ == "__main__":
    print_persons("file1.json")
