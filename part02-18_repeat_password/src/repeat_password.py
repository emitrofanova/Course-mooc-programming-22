# Write your solution here
pwd = input("Password: ")

while True:
    pwd2 = input("Repeat password: ")
    if pwd != pwd2:
        print("They do not match!")
    else:
        print("User account created!")
        break