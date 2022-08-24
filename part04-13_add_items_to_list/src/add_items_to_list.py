# Write your solution here
num_items = int(input("How many items: "))
l = []
i = 0
while num_items > 0:
    i += 1
    item = int(input(f"Item {i}: "))
    l.append(item)
    num_items -= 1
print(l)
