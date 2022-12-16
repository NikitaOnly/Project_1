# Сгенерировать n множеств (нумерацию начать с 1).
# Вывести элементы, которые входят во все множества с номерами, кратными трём, но не входят в первое множество.
from random import randint
import random
number_of_sets = int(input('Введите количество множеств'))
number_of_set = []
sets_1 = set()
sets_full = set()
for i in range(1, number_of_sets + 1):
    my_sets = set((random.randint(1, 50)) for j in range(6))
    print('Множество № ', i, my_sets)
    if i == 1:
        sets_1.update(my_sets)
    elif i % 3 == 0:
        sets_full.update(my_sets)
print(sets_1, sets_full)
dif_set = sets_full.difference(sets_1)
print()
for k in dif_set:
    number_of_set.append(k)
print('Список множеств, которые входят во все множества с номерами, \n'
      'кратными трем, но не входят в первое множество: \n', number_of_set)