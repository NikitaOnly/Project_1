# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
dict_of_words = {}
for i in range(int(input('Введите количество строк' ))):
    line = input().split()
    for word in line:
        dict_of_words[word] = dict_of_words.get(word, 0) + 1
count = max(dict_of_words.values())
most_frequent_word = [i for i, word in dict_of_words.items() if word == count]
for i in dict_of_words:
    print()
print(dict_of_words.items())