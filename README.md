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

## Environment Variables

The project uses environment variables to store sensitive information. Follow the steps below to set up your environment:

1. Create a file named `.env` in the root directory of the project.
2. Copy the contents from `.env.sample` into `.env`.
3. Replace the values in `.env` with your actual environment variable values.

**Note:** Make sure not to commit your `.env` file to version control. It should be listed in the `.gitignore` file.

## Running the Application

1. Set up the environment variables as mentioned in the previous section.
2. Start the development server:

`python manage.py runserver`