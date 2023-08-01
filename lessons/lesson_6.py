# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится.

n = int(input('Enter the number of the Fibonacci number: '))
a, b = 0, 1
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
print(c)

# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).

number = int(input('Enter a positive integer: '))
origin_num = number
reversed_num = 0

while number > 0:
    reversed_num = (reversed_num * 10) + (number % 10)
    number = number // 10

if reversed_num == origin_num:
    print('The number is a palindrome')
else:
    print('The number isn`t a palindrome')

# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
#  вместо чисел кратных 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
