Cоздание виртуального окружения:

1. Создаем папку для виртуального окружения в PowerShell набрать:
 
    python3 -m venv .venv

2. Изменить политику, в PowerShell набрать:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Войти в папку окружения (env), выполнить команду

    .venv\Scripts\activate.ps1

4. Нажать Ctrl + Shift + P, набрать Python: Select Interpreter
Указать нужный путь к python.exe в папке только что созданного окружения .venv, это отобразится внизу в панели состояния.Теперь можно устанавливать модули только для конкретного проекта.

5. Для выхода, в PowerShell выполнить

    deactivate