# Write your solution here
def new_person(name: str, age: int):
    if name == "" or len(name.split()) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("Wrong input")
    else:
        return (name, age)

if __name__ == "__main__":
    name_inp = input("Name: ")
    age_inp = int(input("Age: "))
    print(new_person(name_inp, age_inp))