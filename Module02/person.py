class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self):
        print(f"hi, {self.name}")

    def _greet():
        print("hi")


john = Person("John")
john.greet()

Person._greet()


class ClassName:
    # Class body
    pass
