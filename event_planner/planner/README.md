# Event Planner app

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install fastapi python-multipart beanie uvicorn passlib bcrypt==4.0.1 pydantic[email] pydantic-settings python-jose[cryptography] httpx pytest
# MacOS or Linux
pip freeze > requirements.txt
# Windows Powershell
# pip freeze | Out-File -Encoding UTF8 requirements.txt

# pip uninstall -r requirements.txt -y
```

```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```
