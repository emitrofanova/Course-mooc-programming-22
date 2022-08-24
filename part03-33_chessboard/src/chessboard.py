# Write your solution here

def chessboard(num):
    i = 1
    j = 1
    while i <= num:
        while j <= num:
            if i % 2 == 1:
                if j % 2 == 1:
                    print(1, end='')
                else:
                    print(0, end='')
            else:
                if j % 2 == 1:
                    print(0, end='')
                else:
                    print(1, end='')
            j += 1
        print()
        j = 1
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
