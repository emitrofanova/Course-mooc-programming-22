# Write your solution here
num = float(input("Please type in a number: "))
print("Integer part:", int(num))
print("Decimal part:", int((num - int(num))*1000000)/1000000)