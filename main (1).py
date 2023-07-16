# list
# numbers = []
# numbers_1 = list()

# numbers = [1, 3, 25, 7, 2, 7]

# print(numbers)
# print(numbers[0])
# #
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])

# # перебираем по индексам
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
# # перебираем по значениям
# for number in numbers:
#     print(number, end=" ")
#
# print()

##

# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])
#
# # разложение списка (декомпозиция)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

##########
#
import random

# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
# print(numbers)
# # append(item): добавляет элемент item в конец списка
#
# numbers.append(2222)
# print(numbers)
# #
# # # insert(index, item): добавляет элемент item в список по индексу index
# #
# numbers.insert(1, 3333)
# print(numbers)
# #
# # # extend(items): добавляет набор элементов items в конец списка
# #
# numbers.extend([2, 3, 4])
# print(numbers)
#
# numbers += [1, 2, 3, 4]
# print(numbers)
# #
# # # remove(item): удаляет элемент item. Удаляется только первое вхождение элемента.
# # # Если элемент не найден, генерирует исключение ValueError
# #
# numbers.remove(2222)
# print(numbers)
# #
# # # clear(): удаление всех элементов из списка
# #
# # numbers.clear()
# # print(numbers)
# #
# # del numbers
# # print(numbers)
# #
# # # index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
# #
# print(numbers.index(2))
# #
# # # pop([index]): удаляет и возвращает элемент по индексу index.
# # # Если индекс не передан, то просто удаляет последний элемент.
# #
# print(numbers.pop(0))
# print(numbers)
#
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): возвращает количество вхождений элемента item в список
# #
# print(numbers.count(3))

# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию.
# Но с помощью параметра key мы можем передать функцию сортировки.
# sorted(list, [key]): возвращает отсортированный список

# v1
# numbers.sort()
# print(numbers)
# v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# # v1
# # people.sort()
# # print(people)
# # v2
# # people.sort(key=str.lower)
# # print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# # reverse(): расставляет все элементы в списке в обратном порядке
#
# numbers.reverse()
# print(numbers)
#
# # copy(): копирует список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Кроме того, Python предоставляет ряд встроенных функций для работы со списками:
# #
# # len(list): возвращает длину списка
#
# print(len(numbers))
#
# # min(list): возвращает наименьший элемент списка
#
# print(min(numbers))
#
# # max(list): возвращает наибольший элемент списка
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
#
# letters = ["ab", "ac"]
# print(len(letters[0]))
# print(max(letters))

####
###
# nums = ["one", "two", "three", "four"]
# result = ", ".join(nums)
# print(nums)
# print(result)
# #
# revert_to_nums = result.split(", ")
# print(revert_to_nums)
#
# text = "one, two three, four"
# result = text.split()
# print(result)
# result = text.split(", ")
# print(result)

##################
##
# v1
# matrix = [
#     [1, 3, 2],
#     [1, 4],
#     # 1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
#
# print(matrix[0][1])
# print(matrix[2][1][1])
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#
# matrix = []
#
# print(matrix)
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
# #
# # v1
# print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#############
# создать список из 10 случайных чисел
# поменять местами минимальное значение с максимальным
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]

# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 100))
#
# print(numbers)
#
# # min_value = min(numbers)
# # max_value = max(numbers)
# #
# # # v1
# # min_value_index = numbers.index(min_value)
# # max_value_index = numbers.index(max_value)
# #
# # numbers[min_value_index] = max_value
# # numbers[max_value_index] = min_value
#
# # v2
# numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))] = max(numbers), min(numbers)
# #
# print(numbers)

###########
# text = "hello how are you? fine thank you! hello world. some text."
# text_v1 = text.split(". ")
# for i in range(len(text_v1)):
#     text_v1[i] = text_v1[i].capitalize()
#
# print(text_v1)
#
# text_v2 = text_v1[0].split("! ")
# print(text_v2)

# text = ". ".join(text_v1)
# print(text)

############
# text = "hello World test"
# text = text[0].upper() + text[1:]
# print(text)

############
import random

words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]

secret_word = words[random.randint(0, len(words) - 1)]
# print(secret_word)

user_word = ["_"] * len(secret_word)
# print(user_word)
attempts_counter = 0

while True:
    # v1
    # if "".join(user_word) == secret_word:
    #     print(f"You guessed secret word! {secret_word}")
    #     break
    # v2
    if "".join(user_word).find("_") == -1:
        print(f"\nYou guessed secret word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
        break

    print(" ".join(user_word))

    letter = input("Enter a letter: ").strip().lower()
    attempts_counter += 1

    if not letter.isalpha() or len(letter) != 1:
        print("Please enter only letter!")
        continue

    for i in range(len(secret_word)):
        if letter == secret_word[i].lower():
            user_word[i] = letter
