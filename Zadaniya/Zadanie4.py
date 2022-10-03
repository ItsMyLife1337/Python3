#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    # Вводиться строка с буквами или числами
    strok = input("Введите строку: ")
    return strok


def test_input(strok):
    # Проверяем, возможно ли значение strok привести к числу
    if type(strok) == int:
        return True
    elif strok.isnumeric():
        return True
    else:
        return False


def str_to_int(strok):
    # Идёт преобразование strok к целочисленному формату
    a = int(strok)
    return a


def print_int(strok):
    # Выводим значение на экран
    print(strok)


if __name__ == '__main__':
    strok = get_input()
    proverka = test_input(strok)
    if proverka is True:
        print_int(str_to_int(strok))
    else:
        print("Введённая строка не является числом")
