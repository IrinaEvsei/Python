# -*- coding: utf-8 -*-

def main():
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")
    d = input("Введите D: ")

    print("Уравнение: {}x + {}y + {}z = {}".format(a, b, c, d))

    count = 0
    answers = []
    for i in range(1, d):
        for j in range(1, d):
            for k in range(1, d):
                if i * a + j * b + k * c == d:
                    count += 1
                    answers.append("{}-ый набор: {}, {}, {}".format(count, i, j, k))

    print("Всего решений: {}".format(count))
    for i in answers:
        print(i)


main()