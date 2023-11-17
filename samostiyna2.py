def input_matrix(n):
    matrix = []
    print("Елементи матриці", n, "x", n, ":")
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            return None
        matrix.append(row)
    return matrix

def min_el(matrix):
    n = len(matrix)
    max_el = [max(row) for row in matrix]
    min_among_max = min(max_el)
    return min_among_max

n = int(input("Розмір матриці: "))
new_matrix = input_matrix(n)
if new_matrix is not None:
    result = min_el(new_matrix)
    if result is not None:
        print(f"Результат : {int(result)}")

