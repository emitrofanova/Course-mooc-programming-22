# Write your solution here
# Write your solution here
def ask_command():
    dct = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            return "quitting..."
        if command == 1:
            first(dct)
        if command == 2:
            second(dct)

def first(dct):
    name = input("name: ")
    if name in dct:
        for i in dct[name]:
            print(i)
    else:
        print("no number")

def second(dct):
    name = input("name: ")
    number = input("number: ")
    if name not in dct:
        dct[name] = [number]
    else:
        dct[name].append(number)
    print("ok!")

print(ask_command())
