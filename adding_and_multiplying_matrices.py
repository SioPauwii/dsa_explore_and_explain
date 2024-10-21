# %%
def addMatrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('The matrices must be of same dimensions!')
        return None
    
    output = []
    for i in range(len(matrix1)):
        rows = []
        for j in range(len(matrix1[0])):
            sumRes = matrix1[i][j] + matrix2[i][j]
            rows.append(sumRes)
        output.append(rows)
    return output

def multiplyMatrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print('The number of of collumns for the first matrix and the number of rows of the second matrix must be the same!')
        return None

    output = []
    for i in range(len(matrix1)):
        rows = []
        for j in range(len(matrix2[0])):
            prodOut = 0
            for k in range(len(matrix2)):
                prodRes = matrix1[i][k] * matrix2[k][j]
                prodOut += prodRes
            rows.append(prodOut)
        output.append(rows)
    return output

print('Print the dimension of your first matrix:')
rows1 = int(input('No. of rows: '))
cols1 = int(input('No. of columns: '))

print('\nEnter your values:')
matrix1 = []

for i in range(rows1):
    print(f'Row {i + 1}: ')
    rows1 = []
    for j in range(cols1):
        rows1.append(int(input()))
    matrix1.append(rows1)

print('\nMatrix 1: ')
for row in matrix1:
    print(row)

print('Print the dimension of your second matrix:')
rows2 = int(input('No. of rows: '))
cols2 = int(input('No. of columns: '))

print('\nEnter your values:')
matrix2 = []

for i in range(rows2):
    print(f'Row {i + 1}: ')
    rows2 = []
    for j in range(cols2):
        rows2.append(int(input()))
    matrix2.append(rows2)

print('\nMatrix 2: ')
for row in matrix2:
    print(row)

operation = int(input('\nChoose your operation:\n1: Addition\n2: Multiplication\n\n:'))

print('\nMatrix 1: ')
for row in matrix1:
    print(row)

print('\nMatrix 2: ')
for row in matrix2:
    print(row)

if operation == 1:
    output = addMatrix(matrix1, matrix2)
    print('\nSum of the matrix is: ')
    for row in output:
        print(row)
elif operation == 2:
    output = multiplyMatrix(matrix1, matrix2)
    print('\nProduct of the matrix is: ')
    for row in output:
        print(row)
else:
    print('\nInvalid operation')