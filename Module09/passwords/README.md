# Hashing passwords

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install passlib[bcrypt]
# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt
```

```powershell
pip install -r requirements.txt
```
