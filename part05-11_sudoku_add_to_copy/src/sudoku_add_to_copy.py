# Write your solution here

def print_sudoku(sudoku: list):
    cnt = 0
    for i in sudoku:
        cnt += 1
        for j in range(9):
            if i[j] == 0:
                print("_", end=" ")
            else:
                print(i[j], end= " ")
            if j == 2 or j == 5:
                print(" ", end="")
        print()
        if cnt == 3 or cnt == 6:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_sudoku = []
    for item in sudoku:
        new_sudoku.append(item[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
