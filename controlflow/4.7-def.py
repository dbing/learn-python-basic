# -*- coding: utf-8 -*-

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def parrot(name, state='active', action='voom', color='yellow'):
    print("It's name: ", name)
    print("It's state ", state, "!")
    print("It's action ", action)
    print("It's color ", color)

# parrot('Kitty')
# parrot(name='Kitty')
# parrot(name='Kitty', action='VOOOOOM')
# parrot(action='VOOOOOM', name='Kitty')
# parrot('Kitty', 'cry', 'jump')
# parrot('Kitty', state='smile')


# 错误用法
parrot()
parrot(name='Kitty', 'VOOOOOM')
parrot('Kitty', name='Kitty')
parrot(actor='John Cleese')
