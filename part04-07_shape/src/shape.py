# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def shape(width, ch1, height, ch2):
    i = 1
    while i <= width:
        line(i, ch1)
        i += 1
    while height > 0:
        line(width, ch2)
        height -= 1

def line(num, st):
    if st == "":
        print(num * "*")
    else:
        print(num * st[0])

if __name__ == "__main__":
    shape(5, "x", 2, "o")