# -*- coding: utf-8 -*-

def main():
    n1 = int(input("Введите N: "))
    n2 = int(input("Введите n: "))

    print("Количество простых чисел: " + str(len(find_primes(n1))))
    print("Простые числа: " + str(find_primes(n1))[1:-1])
    for i in range(2, n2 + 1):
        print(str(i) + "-ая степень: " + str(elevate(i, find_primes(n1)))[1:-1])


def find_primes(n):
    ans = []

    for i in range(2, n):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True

        if not flag:
            ans.append(i)

    return ans


def elevate(power, array):
    ans = array
    for i in range(len(ans)):
        ans[i] = ans[i] ** power

    return ans


main()
