# Write your solution here
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
print("Number of groups formed:", (students - 1) // size + 1)
