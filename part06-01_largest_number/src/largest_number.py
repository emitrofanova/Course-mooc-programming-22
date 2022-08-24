# write your solution here
def largest():
    with open("numbers.txt") as file:
        max = 0
        for line in file:
            number = int(line)
            if number > max:
                max = number
    return max

if __name__ == "__main__":
    print(largest())
