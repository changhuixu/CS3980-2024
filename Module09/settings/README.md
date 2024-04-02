# Settings and Environment Variables

[FastAPI doc](https://fastapi.tiangolo.com/ru/advanced/settings/)

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install  pydantic-settings
pip install fastapi uvicorn
# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt

# pip uninstall -r requirements.txt -y
```

```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables

```bash
$ export MY_NAME="Awesome"
$ echo "Hello $MY_NAME"
Hello Awesome
```

```powershell
> $Env:MY_NAME = "Awesome"
> echo "Hello $Env:MY_NAME"
```

environment variable will disappear once the terminal is closed.

```powershell
$ENV:Admin_Email="test@email.com"
python .\main_pydantic.py
Remove-Item Env:admin_email
```

Shell Environment prevails `.env` values

## In FastAPI

```powershell
pip install fastapi uvicorn httpx pytest
# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt
uvicorn app:app --reload
pytest
```
