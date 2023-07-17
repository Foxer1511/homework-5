#Завдання 1
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

import random

NUMB_SIZE = 10
numbers = []
n = 0
p = 0
y = 0
u = 1
k = 0
index_start = 0
index_end = 0

for i in range(NUMB_SIZE):
    numbers.append(random.randint(-99, 99))
print("Список")
print(numbers, "")
# ■ Добуток елементів між мінімальним та максимальним елементом;
min_value = min(numbers)
max_value = max(numbers)
min_max = min(numbers) * max(numbers)

for number in numbers:
    # ■ Суму негативних чисел;
    if number < 0:
        n += number
    # ■ Суму парних чисел;
    if number/2:
        p += number
    # ■ Суму непарних чисел;
    if number%2 == 1:
        y += number
    # ■ Добуток елементів з кратними індексами 3;
    if number%3 == 0:
        u = number * u

# # ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
for g in range(len(numbers)):
    if numbers[g] > 0:
        index_start = g
        break
for g in range(len(numbers) - 1, - 1, -1):
    if numbers[g] > 0:
        index_end = g
        break
my_sum = 0
for g in range(index_start + 1, index_end):
    my_sum += numbers[g]

print("")
print("Сума негативних чисел ", n)
print("Сума парних чисел ", p)
print("Сума непарних чисел ", y)
print("Добуток елементів з кратними індексами 3 ", u)
print("Добуток елементів між мінімальним та максимальним елементом ", min_max)
print("Сумa елементів, що знаходяться між першим та останнім позитивними елементами. ", my_sum)
print()

#Завдання 2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

print("Cписок цілих, що містить лише парні числа")
for number in numbers:
    if number%2 == 0:
        print(number, end=" ")
print()
print("Cписок цілих, що містить лише непарні числа")
for number in numbers:
    if number%2 == 1:
        print(number, end=" " )
print()
print("Cписок цілих, що містить лише негативні числа")
for number in numbers:
    if number < 0:
        print(number, end=" " )
print()
print("Cписок цілих, що містить лише позитивні числа")
for number in numbers:
    if number > 0:
        print(number, end=" " )
#!!!!




