# Getting Started
* Install Robot Framework in a Virtual Environment
```bash
python -m venv .venv
```

* Activate or Deactivate
```bash
.venv\Scripts\activate.bat
# or
.venv\Scripts\deactivate.bat
```

* Install robot framework
```bash
pip install robotframework
robot --version
```

* List package library
```bash
pip list
```

# Install dependency
* Poetry
* Selenium library
### Tool for management
* Poetry is a tool for dependency management and packaging in Python
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python
```

* Set PATH for poetry
```
Choose Edit variable environment -> Add PATH
```

* Check robot framework
```bash
poetry --version
```

* Virtual Environments folder: Poetry will save the virtual enviromentson in the .poetry/envs folder. You can change that setting and store your virtual environment in the project folder by running
```bash
poetry config virtualenvs.in-project true
```
### Selenium