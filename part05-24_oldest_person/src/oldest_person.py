# Write your solution here
def oldest_person(people: list):
    max = 2022
    for i in people:
        if i[1] < max:
            max = i[1]
            answ = i[0]
    return answ

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
