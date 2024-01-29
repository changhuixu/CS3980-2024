# help(print)

# functools

import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee():
    """some help"""
    print("Whee!")


print(say_whee.__name__)
print(help(say_whee))
