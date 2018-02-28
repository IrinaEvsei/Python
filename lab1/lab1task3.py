# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def main():
    s = raw_input("Введите последовательность: ")
    array = map(int, s.split())

    find_number_of_min_max(array)
    print(define_monotone(array))

    sorted_array = merge_sort(array)
    print(sorted_array)

    for i in range(len(sorted_array) + 1):
        temp = ""
        for j in range(i):
            temp += str(sorted_array[j]) + " "

        print(temp)


def find_number_of_min_max(array):
    for i in range(len(array) - 1):
        count_min = 0
        count_max = 0

        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                count_min += 1

            if array[j] > array[i]:
                count_max += 1

        print("Количество чисел, больших {} - {}".format(array[i], count_max))
        print("Количество чисел, меньших {} - {}".format(array[i], count_min))


def define_monotone(array):
    temp = False

    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            temp = True

    if not temp:
        return "Монотонно возрастающая"
    else:
        for i in range(0, len(array) - 1):
            if array[i] < array[i + 1]:
                temp = False

        if temp:
            return "Монотонно убывающая"
        else:
            return "Не обладает свойством монотонности"


def merge(a, b):
    c = []

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a

    return c


def merge_sort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) / 2
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a, b)


main()