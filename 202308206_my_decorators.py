# Задания:
# Декоратор для замера времени выполнения функции (done)
# узнать количество запусков функции (done)
# Декоратор для логирования вызовов функции и аргументов (done)
# Декоратор для проверки аргументов функции на корректность (done)
# Декоратор для кэширования результатов функции, чтобы избежать повторных вычислений.
# Декоратор для ограничения количества вызовов функции в определенный интервал времени.
# Декоратор для авторизации, чтобы проверить доступ к определенным функциям только у авторизованных пользователей.
# Декоратор для перехвата и обработки исключений в функции.

from datetime import datetime as dt


def processing_time(function):
    def wrapper(*args):
        start_time = dt.now()
        function(*args)
        process_time = dt.now() - start_time
        print(f"Process time is {process_time} sec\n")

    return wrapper


@processing_time
def summ_to(n):
    for i in range(n):
        print(i+1, dt.now())


def logger(fn):
    def wrapper(*args):
        fn(*args)
        wrapper.counter += 1
        print(f"Function was started {wrapper.counter} times")
    wrapper.counter = 0
    return wrapper


@logger
def summ_to_1(n):
    summ = 0
    for i in range(n):
        summ += i
    print(f"Summ: {summ};  ", end="")


def arguments(fn):
    def wrapper(*args):
        wrapper.ar = []
        for i in args:
            wrapper.ar.append(i)
        fn(*args)
        print(wrapper.ar, "\n")
    return wrapper


@arguments
def summ_to_2(n, m, k):
    summ = 0
    for i in range(n):
        summ += i
    print(f"Summ: {summ}, n={n}, m={m}, k={k};  ", end="")


def verify(fn):
    def inner(*args):
        param = True
        for i in args:
            if type(i) != int:
                print(f"{i} - is not integer argument!")
                param = False
        if param:
            print("Arguments are fine!  ", end="")
            fn(*args)
    return inner


@verify
def summ_3(n, m, k):
    summ = 0
    for i in range(n):
        summ += i
    print(f"Summ: {summ}, n={n}, m={m}, k={k}")


if __name__ == '__main__':
    # processing time decorator
    summ_to(3)
    # counter of function starts
    summ_to_1(5)
    summ_to_1(7)
    summ_to_1(10)
    print()
    # decorator logging of function arguments
    summ_to_2(3, 5, 7)
    # decorator verifying of function arguments
    # summ_3(2, 4, 2.3)  # Arguments with mistake
    summ_3(2, 4, 6)  # working arguments
