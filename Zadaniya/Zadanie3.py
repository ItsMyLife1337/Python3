#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    print("Введите число: ")
    b = 1
    while True:
        a = int(input(">>> "))
        if a == 0:
            break
        else:
            b *= a
    print("Итог перемножения: ", b)


if __name__ == '__main__':
    test()
