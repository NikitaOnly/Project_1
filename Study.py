# Вычислить количество отрицательных элементов под главной диагональю матрицы.
main_matrix = []
rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество стоблцов '))
for i in range(rows):
    matrix = []
    for j in range(columns):
        elements = int(input())
        matrix.append(elements)
    main_matrix.append(matrix)
for i in main_matrix:
    print(i)
print()
low_diagonal = []
for i in range(rows):
    for j in range(columns):
        if i > j:
            low_diagonal.append(main_matrix[i][j])
print(low_diagonal, end=' ')
amount_low_diagonal = []
negative = 0
for i in range(len(low_diagonal)):
    if low_diagonal[i] < 0:
        negative += 1
        amount_low_diagonal.append(low_diagonal[i])
print('Количество отрицательных элементов', negative)

