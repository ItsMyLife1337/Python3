#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input('Введите число '))
    if num > 0:
        positive()
    else:
        negative()


def positive():
    print("Число положительное")


def negative():
    print("Число отрицательное")


if __name__ == '__main__':
    test()
