# Copy here code of line function from previous exercise

def square(size, character):
    # You should call function line here with proper parameters
    i = size
    while i > 0:
        line(size, character)
        i -= 1

def line(num, st):
    if st == "":
        print(num * "*")
    else:
        print(num * st[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")