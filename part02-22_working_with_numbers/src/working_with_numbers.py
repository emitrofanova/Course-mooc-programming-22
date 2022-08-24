# Write your solution here
cnt = 0
sum = 0
posit = 0
negat = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    cnt += 1
    sum += num
    if num > 0:
        posit += 1
    else:
        negat += 1

print("... the program asks for numbers")
print("Numbers typed in", cnt)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum / cnt)
print("Positive numbers", posit)
print("Negative numbers", negat)
