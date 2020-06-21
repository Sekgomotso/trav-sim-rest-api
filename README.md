# trav-sim-rest-api

## Instructions:

Download and install python3.7

### Create a virtual environment
1. For virtualwrapper: 
```
mkvirtualenv rest-api
```

To activate:
```
workon rest-api
```

2. For venv: 
```
virtualenv -p python3 rest-api
```
To activate: 
```
source rest-api/bin/activate
```

### Install the modules in requirement.txt 
```
pip3 install -r requirements.txt 
```

### Make migrations
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

### Create superuser
```
python3 manage.py createsuperuser
```

### runserver
```
python3 manage.py runserver
```
### Factors considered determining the technical and architectural choices
Authentication, methods required, status codes, content type and documentation

### What I'd do if I had more time
More research, user friendly and make it secure.
