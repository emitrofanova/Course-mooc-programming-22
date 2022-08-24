# Write your solution here
limit = int(input("Limit: "))
result = "The consecutive sum: 1"
num = 1
sum = 0
while sum < limit:
    sum += num
    if num > 1:
        result += f" + {num}"
    num += 1
result += f" = {sum}"
print(result)
