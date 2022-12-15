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

# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее. Словом считается последовательность непробельных
# символов, идущих подряд.
# Слова разделены одним или большим числом пробелов или символами конца строки.
words = input().split()
dictonary = {}
for i in words:
    if i not in dictonary:
        dictonary[i] = 0
    else:
        dictonary[i] += 1
print(dictonary)
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее. Словом считается последовательность непробельных
# символов, идущих подряд.
# Слова разделены одним или большим числом пробелов или символами конца строки.
