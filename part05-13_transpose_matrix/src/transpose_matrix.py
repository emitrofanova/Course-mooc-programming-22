# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    for item in matrix:
        new_matrix.append(item[:])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = new_matrix[i][j]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transp = transpose(matrix)
    print(matrix)
