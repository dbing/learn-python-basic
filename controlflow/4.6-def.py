# -*- coding: utf-8 -*-

def fib(n):
    """打印一个斐波那契数列直到 n """
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(2000)
