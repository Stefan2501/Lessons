# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
sentence = input('enter a sentence:')
words = [word.strip("!?,.;:") for word in sentence.split()]
longest_word = max(words, key=len)
print('The longest word: ' + longest_word)

# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

string = input('enter a string:')

new_string = ''.join(set(string.replace(' ', '')))
print(new_string)

# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string_2 = input('enter a string:')
lower_count = 0
upper_count = 0
for i in string_2:
    if i.isalpha() and i.isascii():
        if i.islower():
            lower_count += 1
        else:
            upper_count += 1
print(f"quantity of lowercase letters: {lower_count}")
print(f"quantity of uppercase letters: {upper_count}")
