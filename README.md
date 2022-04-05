# dataAnalyze
This is project to collect, analyze, build diagramm and save them in pdf format

How to start working:
1. Clone the repository.
2. Create virtual environment with command: "python -m venv virtual_environment_name" recommend using name ff_env because this name already added to gitignore file.
   However you can create whatever name you want, just add it to gitignore file to avoid your virtual environment to go to repository.
3. Install requirenment using activated virtual environment: "./your_virtual_env_name/Scripts/activate".
4. If you have an execution error, open PowerShell as Administrator and run command "set-executionpolicy remotesigned" and comfirm all changes.
5. Run command: "pip install -r requirements.txt".
6. Depencies installed and you can work now.

How to add your depencies/libraries to project:
1. Make sure you download starting depencies.
2. Install you depencies to virtual environment ("pip install lib_name" while in virtual environment).
3. Run command "pip freeze > requirenments.txt".
4. Push to repository your changes.