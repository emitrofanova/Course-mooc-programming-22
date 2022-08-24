# Write your solution here

def sudoku_grid_correct(sudoku):
    return row_correct(sudoku) and column_correct(sudoku) and block_correct(sudoku)

def row_correct(sudoku: list):
    cnt = 0
    for i in range(1,10):
        for row in sudoku:
            for j in row:
                if i == j:
                    cnt += 1
                    if cnt > 1:
                        return False
            cnt = 0
    return True

def column_correct(sudoku: list):
    cnt = 0
    for i in range(1,10):
        for column in range(9):
            for j in sudoku:
                if i == j[column]:
                    cnt += 1
                    if cnt > 1:
                        return False
            cnt = 0
    return True

def block_correct(sudoku: list):
    cnt = 0
    for i in range(1,10):
        for row in range(0, 3):
            for column in range(0, 3):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(0, 3):
            for column in range(3, 6):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(0, 3):
            for column in range(6, 9):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(3, 6):
            for column in range(0, 3):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(3, 6):
            for column in range(3, 6):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(3, 6):
            for column in range(6, 9):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(6, 9):
            for column in range(0, 3):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(6, 9):
            for column in range(3, 6):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    for i in range(1,10):
        for row in range(6, 9):
            for column in range(6, 9):
                if i == sudoku[row][column]:
                    cnt += 1
                    if cnt > 1:
                        return False
        cnt = 0
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
