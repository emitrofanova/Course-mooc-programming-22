# Write your solution here
def line(num, st):
    if st == "":
        print(num * "*")
    else:
        print(num * st[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")