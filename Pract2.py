from random import randint
from datetime import datetime
# lambda
# 1
lst = [(randint(0,9), randint(0,9)) for i in range(6)]

def sort_lst1(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_lst1(lst))
# 2
lst = ['привет', 'a', 'кто']
def sort_lst2(lst):
    return sorted(lst, key=lambda x: len(x), reverse=True)

# 3
def incrementer(start_val, modulator, productor,addition):
    r_var = start_val
    m = modulator
    a = productor
    c = addition
    def inner():
        nonlocal r_var
        nonlocal m
        nonlocal a
        nonlocal c
        r_var = (a * r_var + c) % m
        return r_var
    return inner
test_func = incrementer(7, 10,7,7)

# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())

# Generator
# 1, 2
def rand_progression(start_val, modulator, productor,addition):
    r_var = start_val
    while True:
        yield r_var
        r_var = (productor * r_var + addition) % modulator


r_p = rand_progression(7, 10,7,7)
# print(next(r_p))
# print(next(r_p))
# print(next(r_p))
# print(next(r_p))

# 3
def rand_progression2(start_val, modulator, productor):
    r_var = start_val
    while True:
        addition = (yield)
        r_var = (productor * r_var + addition) % modulator
        print(r_var)
        yield r_var

r_p2 = rand_progression2(7, 10,7)
next(r_p2)

for i in range(10):
    r_p2.send(7)
    print(i)


# decorators
# 1

def test_foo(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

def fib(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result

def decorator_func1(func):
    fib.counter = 0
    fib.were_called = []
    fib.cache = {}
    def wrapper(*args):
        start_time = datetime.now()
        if args in fib.cache:
            a = fib.cache[args]
        else:
            a = func(*args)
            fib.cache[args] = a
        fin_time = datetime.now()
        print('it took ' + str(fin_time - start_time))
        fib.counter += 1
        fib.were_called.append(datetime.now())
        print(f"job was done {fib.counter} time(s)")
        return a
    return wrapper


decorated_func_1 = decorator_func1(fib)

print(decorated_func_1(4))
print(decorated_func_1(5))
print(fib.cache)
decorated_func_1(1000000)
print(fib.were_called)


