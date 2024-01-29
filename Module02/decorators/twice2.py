# Decorating Functions With Arguments


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee():
    """some help"""
    print("Whee!")


say_whee()


@do_twice
def greet(name):
    print(f"Hello {name}")


greet("World")
