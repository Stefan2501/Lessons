# *****СПИСКИ*****

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар. Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

lst = input('enter a string of numbers:').split()
counter = {}
count_pairs = 0

for num in lst:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

for count in counter.values():
    if count > 1:
        count_pairs += count * (count - 1) // 2

print(count_pairs)

# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

elements = input('enter a list of element:').split()
unique_elements = set()
repeated_elements = set()
for element in elements:
    if element in unique_elements:
        repeated_elements.add(element)
    else:
        unique_elements.add(element)

unique_set = unique_elements - repeated_elements

print(list(unique_set))

# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

lst_int = [1, 0, 2, 3, 4, 0, 5, 0, 1]
zero_index = 0
for i in range(len(lst_int)):
    if lst_int[i] != 0:
        lst_int[zero_index], lst_int[i] = lst_int[i], lst_int[zero_index]
    zero_index += 1
print(lst_int)

# *****КОРТЕЖИ*****

# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.

my_list = ['a', 'b', 'c']
print(tuple(my_list))

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.

my_tuple = 'a', 'b', 'c'
print(list(my_tuple))

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.

a, b, c = 'a', 2, 'python'
print(a, b, c)

# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

tpl = ((1, 2, 3),)
for i in tpl[0]:
    print(i)
print('tpl length:', len(tpl))

# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

a = int(input('enter a:'))
b = int(input('enter b:'))
while b != 0:
    a, b = b, a % b
print(max(a, b))

# *****CЛОВАРИ*****

# Города
# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
# в какой стране он находится. Учтите, что бывают ситуации когда город с таким называнием бывает в
# разных странах (Брест есть в Беларуси и Франции).
#
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
#
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.


n = int(input('enter number of country:'))
world = {}
for _ in range(n):
    country_cities = input('enter country and ist cities:').split()
    country, cities = country_cities[0], country_cities[1:]
    for city in cities:
        world.setdefault(city, []).append(country)
m = int(input('enter number of requests:'))
for _ in range(m):
    city = input('enter city:')
    if city in world:
        countries = ', '.join(world[city])
        print(f"{city} city is located in the following country(countries): {countries}")
    else:
        print((f"{city} сity not found"))

# *****МНОЖЕСТВА*****

# Во входной строке записан текст. Словом считается последовательность непробельных символов идущих подряд.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

text = "Во входной  строке записан текст. Словом считается    последовательность\n непробельных символов идущих подряд"
words = text.replace("\n", " ").split(" ")
print(len(set(words)))

# Даны два списка чисел. Cколько различных чисел содержится одновременно как в первом списке, так и во втором.

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [4, 5, 6, 7, 8]
print(len(set(lst_1) & set(lst_2)))

# Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков.

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(len(set(lst1) ^ set(lst2)))

# Языки
#
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
#
# Входные данные
#
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел
# идет Mi строк, содержащих названия языков, которые знает i-й школьник.

n = int(input('enter number of students:'))
languages = []
for i in range(n):
    m = int(input('enter number of languages a student knows:'))
    langs = []
    for j in range(m):
        langs.append(input('enter the language the student knows:'))
    languages.append(set(langs))

all_langs = languages[0]
any_langs = languages[0]
for lang_set in languages[1:]:
    all_langs &= lang_set
    all_langs |= lang_set

print('Number of languages known by all students:', len(all_langs))
print(all_langs)
print('Number of languages known by any student:', len(any_langs))
print(any_langs)

# *****ГЕНЕРАТОРЫ СПИСКОВ*****

# Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']
a = [i + j for i in ['x', 'y'] for j in ['y', 'z', 'v']]

# Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz']
b = a[::2]

# Используйте генератор списков чтобы получить следующий ['1x', '2x', '3x', '4x']
c = [str(i) + 'x' for i in range(1, 5)]

# Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.
print(c.pop(c.index('2x')))

# Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
c_copy = c + ['2x']

# *****ГЕНЕРАТОРЫ СЛОВАРЕЙ*****

# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
# а значениями кубы этих чисел.
dct = {i: i ** 3 for i in range(1, 21)}

# Создайте множество с помощью генератора множеств, состоящее из общих делителей чисел 1000 и 9000.
s = {i for i in range(1, 1001) if 1000 % i == 0 and 9000 % i == 0}


# *****ГЕНЕРАТОРЫ*****

# Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
# Пример для числа 3:
#    0  0  0  0
#    0	1  2  3
#    0	2  4  6
#    0	3  6  9

def multiplication_table(d):
    for i in range(d + 1):
        row = [str(i * j) for j in range(d + 1)]
        yield "\t".join(row)
