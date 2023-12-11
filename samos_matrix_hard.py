import copy

def input_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            el = float(input(f"Елемент [{i + 1}][{j + 1}]: "))
            row.append(el)
        matrix.append(row)
    return matrix

def print_matrix(matrix, name="Матриця"):
    print(f"{name}:")
    for row in matrix:
        print(' '.join(f'{elem:.0f}' for elem in row))

def multiply_matrices(matrix1, matrix2):
    result = []
    if len(matrix1[0]) != len(matrix2):
        print("Не можна перемножити")
        return result

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(0)
        result.append(row)

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def multiply_matrix_vector(matrix, vector):
    result = 0
    if len(matrix[0]) != len(vector):
        print("Не можна перемножити")
        return result

    for i in range(len(matrix)):
        row_result = 0
        for j in range(len(vector)):
            row_result += matrix[i][j] * vector[j]
        result += row_result

    return int(result)

def swap_rows(matrix, row1, row2):
    if 0 <= row1 < len(matrix) and 0 <= row2 < len(matrix):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
        return matrix 
    else:
        print("Введено не правильні координати")
        return matrix  
    
def swap_columns(matrix, col1, col2):
    if 0 <= col1 < len(matrix[0]) and 0 <= col2 < len(matrix[0]):
        for i in range(len(matrix)):
            matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
        return matrix  
    else:
        print("Введено не правильні координати")
        return matrix  
    
def get_row(matrix, row_index):
    if 0 <= row_index < len(matrix):
        return matrix[row_index]
    else:
        print("Введено не правильний номер рядка")
        return None  

def multiply_vector_by_scalar(vector, scalar):
    result = [elem * scalar for elem in vector]
    return result

def subtract_vector_from_rows(matrix, vector):
    if len(matrix[0]) != len(vector):
        print("Не можна відняти")
        return matrix

    result = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i][j] -= vector[j]

    return result

def upper_triangular(matrix):
    upper_triangular_matrix = copy.deepcopy(matrix)
    for col in range(len(upper_triangular_matrix[0])-1):
        for row in range(col + 1, len(upper_triangular_matrix)):
            if upper_triangular_matrix[col][col] != 0:
                factor = upper_triangular_matrix[row][col] / upper_triangular_matrix[col][col]
                for i in range(col, len(upper_triangular_matrix[0])):
                    upper_triangular_matrix[row][i] -= factor * upper_triangular_matrix[col][i]

    return upper_triangular_matrix

def matrix_rank(matrix):
    rank = 0
    temp_matrix = copy.deepcopy(matrix)
    num_rows = len(temp_matrix)
    num_cols = len(temp_matrix[0])

    for col in range(num_cols):
        if rank >= num_rows:
            break

        pivot_row = rank
        while pivot_row < num_rows and temp_matrix[pivot_row][col] == 0:
            pivot_row += 1

        if pivot_row < num_rows:
            temp_matrix = swap_rows(temp_matrix, rank, pivot_row)
            if temp_matrix[rank][col] != 0:
                divisor = temp_matrix[rank][col]
                temp_matrix[rank] = [elem / divisor for elem in temp_matrix[rank]]

            for row in range(rank + 1, num_rows):
                factor = temp_matrix[row][col] / temp_matrix[rank][col]
                temp_matrix[row] = [elem - factor * temp_matrix[rank][index] for index, elem in enumerate(temp_matrix[row])]

            rank += 1

    return rank

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Визначник не можливо визначити")
        return None

    n = len(matrix)

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        return (
            matrix[0][0] * matrix[1][1] * matrix[2][2] +
            matrix[0][1] * matrix[1][2] * matrix[2][0] +
            matrix[0][2] * matrix[1][0] * matrix[2][1] -
            matrix[0][2] * matrix[1][1] * matrix[2][0] -
            matrix[0][0] * matrix[1][2] * matrix[2][1] -
            matrix[0][1] * matrix[1][0] * matrix[2][2]
        )
    else:
        det = 0
        for col in range(n):
            sign = (-1) ** col
            sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += sign * matrix[0][col] * determinant(sub_matrix)
        return det

rows1 = int(input('Введіть кількість рядків в першій матриці: '))
columns1 = int(input('Введіть кількість стовпців в першій матриці: '))


rows2 = int(input('Введіть кількість рядків в другій матриці: '))
columns2 = int(input('Введіть кількість стовбців в другій матриці: '))

matrix1 = input_matrix(rows1, columns1)
original_matrix1 = copy.deepcopy(matrix1)


if columns1 != rows2:
    print("Матриці не можна перемножувати")
else:
    matrix1 = input_matrix(rows1, columns1)
    matrix2 = input_matrix(rows2, columns2)

    print_matrix(matrix1, "Матриця 1")
    print_matrix(matrix2, "Матриця 2")

    result_matrix = multiply_matrices(matrix1, matrix2)

    if result_matrix:
        print_matrix(result_matrix, "Результат множення матриць")

rows_vector = int(input('Введіть кількість рядків для вектора: '))
vector = []
for i in range(rows_vector):
    el = float(input(f"ВВедіть елемент {i + 1} для вектора: "))
    vector.append(el)

result_vector = multiply_matrix_vector(matrix1, vector)

if result_vector:
    print("Результат множення матриці на вектор:")
    print(result_vector)

cof_1_for_swap = int(input('Введіть номер першого рядка для перестановки: '))
cof_2_for_swap = int(input('Введіть номер другого рядка для перестановки: '))
result_swap_rows = swap_rows(copy.deepcopy(original_matrix1), (cof_1_for_swap - 1), (cof_2_for_swap - 1))

if result_swap_rows:
    print("Результат перестановки рядків в матриці:")
    print_matrix(result_swap_rows, "Матриця після перестановки")

cof_1_for_swap_col = int(input('Введіть номер першого стовбчика для перестановки: '))
cof_2_for_swap_col = int(input('Введіть номер другого стовбчика для перестановки: '))
result_swap_cols = swap_columns(copy.deepcopy(original_matrix1), (cof_1_for_swap_col - 1), (cof_2_for_swap_col - 1))


if result_swap_cols:
    print("Результат перестановки рядків в матриці")
    print_matrix(result_swap_cols, "Матриця після перестановки")

row_number = int(input('Введіть номер рядка, який потрібно вивести: '))
selected_row = get_row(matrix1, row_number - 1)

if selected_row is not None:
    print(f"Рядок {row_number} матриці:")
    print(' '.join(f'{elem:.0f}' for elem in selected_row))

scalar = int(input('Введіть число: '))
result_vector_by_scalar = multiply_vector_by_scalar(copy.deepcopy(original_matrix1)[0], scalar)

print("Результат множення вектора на число:")
print(*[int(elem) for elem in result_vector_by_scalar])

result_subtracted_rows = subtract_vector_from_rows(matrix1, vector)

if result_subtracted_rows:
    print("Результат віднімання вектора від матриці:")
    print_matrix(result_subtracted_rows, "Матриця після віднімання вектора")

result_upper_triangular = upper_triangular(matrix1)

if result_upper_triangular:
    print("Матриця в верхній трикутній формі:")
    print_matrix(result_upper_triangular, "Верхня трикутна форма")

rank_of_matrix1 = matrix_rank(matrix1)
print(f"Ранг матриці: {rank_of_matrix1}")

det_matrix1 = determinant(matrix1)
if det_matrix1 is not None:
    print(f"Визначник матриці: {det_matrix1}")


