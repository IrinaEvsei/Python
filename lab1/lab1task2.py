# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def main():
    s = raw_input("Введите последовательность: ")
    array = map(int, s.split())
    print(array)

    sec_smallest = second_smallest(array)
    sec_larges = second_largest(array)
    print("Второй минимальный элемент: {}".format(sec_smallest))
    find_entries(sec_smallest, array)
    print("Второй максимальный элемент: {}".format(sec_larges))
    find_entries(sec_larges, array)


def second_smallest(array):
    min_x = array[0]
    sec_min_x = array[1]

    for i in range(2, len(array)):
        if array[i] < min_x:
            sec_min_x = min_x
            min_x = array[i]
        elif array[i] < sec_min_x:
            sec_min_x = array[i]

    return sec_min_x


def second_largest(array):
    max_x = array[0]
    sec_max_x = array[1]

    for i in range(2, len(array)):
        if array[i] > max_x:
            sec_max_x = max_x
            max_x = array[i]
        elif array[i] > sec_max_x:
            sec_max_x = array[i]

    return sec_max_x


def find_entries(number, array):
    index = -1
    count = 0

    for i in range(len(array)):
        if array[i] == number and index == -1:
            index = i + 1

        if array[i] == number:
            count += 1

    print("Количество вхождений числа {} в массив: {}".format(number, count))
    print("Индеск элемента {} в массиве: {}".format(number, index))


main()