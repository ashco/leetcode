def searchMatrix(matrix, target):
    if matrix:
        x, y = len(matrix[0]) - 1, 0

        while x >= 0 and y < len(matrix):
            point = matrix[y][x]

            if point == target:
                return True
            elif point < target:
                y += 1
            else:
                x -= 1

    return False

matrix0 = []

matrix1 = [
    [1, 3, 5, 6],
    [11, 13, 15, 16],
    [21, 23, 25, 36],
    [31, 33, 35, 46],
    [41, 43, 55, 56]
]


print(searchMatrix(matrix0, 23)) # true
print(searchMatrix(matrix1, 23)) # true
print(searchMatrix(matrix1, 17)) # false


# x = 1
# y = 2

