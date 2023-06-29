# Bookshelf Project

Django project for managing books, authors, genres and publications in Bookshelf

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Anyta17/bookshelf.git
cd bookshelf
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
puthon manage.py runserver # starts Django Server
```

## Features

* Authentication functionality for Author/User
* Managing books authors genres & publications directly from website interface
* Powerful admin panel for advanced managing

## 
- Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata bookshelfdata.json`

- You can use the following superuser (or create another yourself):
    - Login: testuser
    - Password: testpassword