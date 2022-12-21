# 1. В текстовый файл построчно записаны фамилия и имя каждого учащегося класса
# и их оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов,
# и посчитать средний балл по классу.
with open('marks.txt', 'r', encoding='utf-8') as file:
    file_read = [line.strip() for line in file.readlines()]
    print(file_read)
    sum = 0
    line = 0
    for i in file_read:
        gr_point = int(i[len(i)-1])
        sum += gr_point
        line += 1
        if gr_point < 3:
            print('Оценка ниже 3 - ', i[:])
print(f'Средний балл: {sum/line}')