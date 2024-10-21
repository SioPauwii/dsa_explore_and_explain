def floodFill(matrix, posX, posY, newColor, ogColor=None, filled=None):

    row, col = len(matrix), len(matrix[0])

    if filled == None:
        filled = set()

    if ogColor == None:
        ogColor = matrix[posX][posY]

    if posX < 0 or posX >= row or posY < 0 or posY >= col or matrix[posX][posY] != ogColor:
        return None
    
    matrix[posX][posY] = newColor
    filled.add((posX, posY))

    highlightIndex(matrix, filled)

    floodFill(matrix, posX + 1, posY, newColor, ogColor, filled)
    floodFill(matrix, posX - 1, posY, newColor, ogColor, filled)
    floodFill(matrix, posX, posY + 1, newColor, ogColor, filled)
    floodFill(matrix, posX, posY - 1, newColor, ogColor, filled)
    floodFill(matrix, posX + 1, posY + 1, newColor, ogColor, filled)
    floodFill(matrix, posX - 1, posY + 1, newColor, ogColor, filled)
    floodFill(matrix, posX - 1, posY - 1, newColor, ogColor, filled)
    floodFill(matrix, posX + 1, posY - 1, newColor, ogColor, filled)



def highlightIndex(matrix, filled=None):
    for i  in range(len(matrix)):
        for j in range(len(matrix[0])):
            if filled and (i, j) in filled:
                print(f'\033[1;45m{matrix[i][j]}\033[0m', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()
    print()


grid = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

print('Initial Grid: ')
highlightIndex(grid)

floodFill(grid, 2, 2, 2)