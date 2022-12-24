# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество символов и слов в ней.
with open('number.txt', 'r') as file:
    line = 0
    symbols = 0
    word = 0
    for i in file:
        line += 1
        word += len(i.split())
        symbols = len(i.strip('\n'))
        print(i, 'см:', len(i), 'сл:', word)
    print(line, 'стр')