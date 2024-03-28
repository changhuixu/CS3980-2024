# Beanie and Motor demos

```powershell
python -m venv venv
./venv/Script/activate
pip install beanie

```

## Settings and Environment Variables

```bash
changhxu@BS-MBSB-L1107 MINGW64 ~
$ export My_Value="Awesome"

changhxu@BS-MBSB-L1107 MINGW64 ~
$ echo "Hello"
Hello

changhxu@BS-MBSB-L1107 MINGW64 ~
$ echo "Hello $My_Value"
Hello Awesome

```

```powershell
PS > $ENV:MY_NAME="Not Awesome"

PS > echo "Hello, $ENV:MY_NAME"
Hello, Not Awesome
PS >
```

The environment variables set in terminal sessions will be discarded once the terminal is closed.

To persist your environment variables, you will need to set them at the system or user level. The best practice is to save sensitive information as environment variables at the user level so that only the App User can access to them.

## Read environment variables using Python

examples are in the `main_os.py` file.

## Beanie Demo

Make sure that you set the environment variables before getting into `venv`. Otherwise, you will just need to re-activated the virtual environment.

**Make sure your `.env` file is not committed in Git.**
