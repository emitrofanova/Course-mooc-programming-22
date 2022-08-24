# write your solution here
def matrix_sum():
    with open("matrix.txt") as file:
        sum_numbers = 0
        for line in file:
            line = line.replace("/n", "")
            line = line.split(",")
            for number in line:
                sum_numbers += int(number)
    return sum_numbers

def matrix_max():
    with open("matrix.txt") as file:
        max = 0
        for line in file:
            line = line.replace("/n", "")
            line = line.split(",")
            for num in line:
                if int(num) > max:
                    max = int(num)
    return max

def row_sums():
    with open("matrix.txt") as file:
        sum_row = []
        for line in file:
            sum_numbers = 0
            line = line.replace("/n", "")
            line = line.split(",")
            for number in line:
                sum_numbers += int(number)
            sum_row.append(sum_numbers)
    return sum_row
    
if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
