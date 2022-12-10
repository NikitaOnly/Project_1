# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.
string = input('Введите строку')
turtle = ()
for i in range(len(string)):
    if string[i] not in turtle:
       turtle += (string[i],)
print(turtle)
turtle_1 = ('hello world')
print(turtle_1)

