# -*- coding: utf-8 -*-

def fib(n):
    """打印一个斐波那契数列直到 n """
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(2000)

print('----------')

def fib2(n):
    """返回一个斐波那契数列直到 n """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)