# FastAPI Todo App

![demo](todo_app.gif)

## 1. Python virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

```powershell
deactivate
```

## 2. pip

Pip is automatically installed during a Python installation. You can verify whether pip is
installed by running the following command in your terminal:

```powershell
python -m pip list
```

The preceding command should return a list of packages installed.

### Basic commands

With pip installed, let's learn its basic commands. To install the FastAPI package with
pip, we run the following command:

```powershell
pip install fastapi
```

On a Unix operating system, such as Mac or Linux, in some cases, the sudo keyword is
prepended to install global packages.

To uninstall a package, the following command is used:

```powershell
pip uninstall fastapi
```

To collate the current packages installed in a project into a file, we use the following
freeze command:

```powershell
pip freeze > requirements.txt
```

The > operator tells bash to save the output from the command into the
`requirements.txt` file. This means that running pip freeze returns an output of
all the currently installed packages.

To install packages from a file such as the `requirements.txt` file, the following
command is used:

```powershell
pip install -r requirements.txt
```

The preceding command is mostly used in deployment.

## uvicorn

We'll begin by installing the dependencies required for our application in the todos
folder we created earlier. The dependencies are the following:

- fastapi: The framework on which we'll build our application.
- uvicorn: An Asynchronous Server Gateway Interface module to run our application.

First, activate your development environment by running the following command in your
project directory:

```powershell
source venv/bin/activate
```

Then, install the dependencies as follows:

```powershell
(venv)$ pip install fastapi uvicorn
```

The next step is to start our application using uvicorn. In your terminal, run the
following command:

```powershell
(venv)$ uvicorn main:app --port 8000 --reload
```

In the preceding command, uvicorn takes the following arguments:

- `file:instance`: The file containing the instance of FastAPI and the name
  variable holding the FastAPI instance.
- `--port PORT`: The port the application will be served on.
- `--reload`: An optional argument included to restart the application on every
  file change.

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt

# pip uninstall -r requirements.txt -y
```
