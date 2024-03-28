import os

name = os.getenv("MY_NAME", "Fall back value")
print(name)
print(f"Hello, {name} from Python")

app_name = os.getenv("APP_NAME")
print(app_name)

app_password = os.getenv("my_password")
print(app_password)
