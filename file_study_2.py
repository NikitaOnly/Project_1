# 2. Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
lines = input('Текст файла''\n')
with open('file.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)
    while True:
        s = input()
        if s == '':
            break
    print(lines)