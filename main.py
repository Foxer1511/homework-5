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
s_negative = 0
s_parni = 0
s_neparni = 0
dob_kr_tri = 1
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
        s_negative += number
    # ■ Суму парних чисел;
    if number/2:
        s_parni += number
    # ■ Суму непарних чисел;
    if number%2 == 1:
        s_neparni += number
    # ■ Добуток елементів з кратними індексами 3;
    if number%3 == 0:
        dob_kr_tri = number * dob_kr_tri

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
print("Сума негативних чисел ", s_negative)
print("Сума парних чисел ", s_parni)
print("Сума непарних чисел ", s_neparni)
print("Добуток елементів з кратними індексами 3 ", dob_kr_tri)
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




