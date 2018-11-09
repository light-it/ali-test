# Selenium test project

## Install

### Install `chromedriver` in your OS 
http://chromedriver.chromium.org/

### In project's directory make virtual environment with python 2
```sh
virtualenv -p python2 venv
```

### Activate virtual environment
```sh
. venv/bin/activate
```

### Install requirments
```sh
pip install -r requirments.txt
```

### Write credentails
Use `env_example` as example.
Copy `env_example` to `.env`. Fill `.env` with your credentails.

## Run

### Activate virtual environment if not yet

### Load credentials
```sh
. .env
```

### Run
```sh
python play_selenium.py
```

