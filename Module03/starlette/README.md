# Intro to starlette

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install starlette uvicorn

# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt
# pip uninstall -r requirements.txt -y
```

To start the server:

```powershell
uvicorn main:app
```

To check if a port is taken:

```powershell
netstat -na | findstr 5001
```
