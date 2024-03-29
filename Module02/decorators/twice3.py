# Returning Values From Decorated Functions


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)
