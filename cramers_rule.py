def determinant(matrix):
    if len(matrix) == 2: 
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:  
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    else:
        raise ValueError("Only 2x2 and 3x3 matrices are supported.")

def cramer_rule(A, B):
    det_A = determinant(A)

    if det_A == 0:
        raise ValueError("The determinant is zero, the system has no unique solution.")
    
    num_vars = len(B)
    solutions = []
    
    for i in range(num_vars):
        A_temp = [row[:] for row in A] 
        for j in range(len(B)):
            A_temp[j][i] = B[j]
        
        det_A_temp = determinant(A_temp)
        
        solutions.append(det_A_temp / det_A)
    
    return solutions


matrixDimension = int(input('Enter the dimension of the matrix (2x2 or 3x3; enter the number of columns[i.e. 2 or 3]): '))

if matrixDimension not in [2, 3]:
    raise ValueError('Only 2x2 and 3x3 is supported')

print('\nEnter your values:')
A = []

for i in range(matrixDimension):
    print(f'Row {i + 1}: ')
    rows1 = []
    for j in range(matrixDimension):
        rows1.append(int(input()))
    A.append(rows1)

print('\nMatrix 1: ')
for row in A:
    print(row)

B = []
print('\nEnter the values of the constants vector (B): ')
for i in range(matrixDimension):
    B.append(int(input()))

print(f'\nVector B: {B}\n')

solution = cramer_rule(A, B)
if(len(solution) == 3):
    print(f'Solution: [x = {solution[0]},  y = {solution[1]}, z =  {solution[2]}]')
else:
    print(f'Solution: [x = {solution[0]},  y = {solution[1]}]')