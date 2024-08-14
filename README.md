# pyapi

## Help

```sh
# initialize virtual env
python3 -m venv .venv

# set virtual environment
source .env/bin/activate`

# install flask
python3 -m pip install flask

# install sqlalchemy
python3 -m pip install flask_sqlalchemy

# install flask_migrate
python3 -m pip install flask_migrate

# create requirements file
python3 -m pip freeze > requirements.txt

# install from requirements
python3 -m pip install -r requirements.txt

# run the application
python3 app.py
```

ensure vscode uses the venv

- CTRL+SHIFT+P
- Search for _Python interpreter_
- Select .venv in this workspace
