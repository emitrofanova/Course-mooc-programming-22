# Write your solution here
l = []
c = 1
while True:
    print("The list is now", l)
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "d":
        l.append(c)
        c += 1
    if action == "r":
        c -= 1
        l.remove(c)
    if action == "x":
        print("Bye!")
        break
