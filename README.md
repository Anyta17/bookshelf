# Bookshelf Project

Django project for managing books, authors, genres and publications in Bookshelf

## Setup Instructions

To set up the project locally, follow these steps:

1. Clone the repository:

  ```
  git clone https://github.com/Anyta17/bookshelf.git
  ```

2. Navigate to the project directory:

  ```
  cd bookshelf
  ```

3. Create a virtual environment and activate it:

  ```
  python -m venv venv
  venv\Scripts\activate
  ```


4. Install the required dependencies:

  ```
  pip install -r requirements.txt
  ```

Note: Replace the empty string with your desired secret key.

**Environment Variables:** You can set up environment variables in the `.env` file to configure the application. For example, the `DJANGO_SECRET_KEY` variable can be set to your desired secret key. By default, the application will use the secret key `django-insecure-9bwy@g=&wuzlpsb#f77z^a41)=fo)03m(1!fv@!km4@$bntxzo` if no value is provided.

5. Apply the database migrations:

  ```
  python manage.py migrate`
  ```

**Note on Database:** Ensure that you have removed the actual database file from the repository, as it should not be stored in version control. Running the migrations will create a new database file.

**Automatically Adding Test User:** To simplify the user's experience, a test user can be added automatically during the migration process. Follow these steps:

1. Create all the objects that should be in the user's database after migration in the usual way.

2. Create a fixture with all the required data:

   ```
   python manage.py dumpdata > fixture_data.json
   ```

3. Create an empty migration related to your app:

   ```
   python manage.py makemigrations APP_NAME --empty
   ```

4. In the created migration file, add the following command to the operations:

   ```python
   from django.db import migrations

   def func(apps, schema_editor):
       from django.core.management import call_command
       call_command("loaddata", "bookshelfdata.json")

   def reverse_func(apps, schema_editor):
       pass

   class Migration(migrations.Migration):

       dependencies = [
           ("APP_NAME", "0001_initial"),  # Replace APP_NAME with your app's name
       ]

       operations = [
           migrations.RunPython(func, reverse_func),
       ]
   ```

6. Start the development server:

  ```
  python manage.py runserver
  ```

## Features


* Authentication functionality for Author/User

* Managing books authors genres & publications directly from website interface

* Powerful admin panel for advanced managing


## 

- Use the following command to load prepared data from fixture to test and debug your code:

  
`python manage.py loaddata bookshelfdata.json`


- You can use the following superuser (or create another yourself):

    - Login: `admin.user`

    - Password: `1qazcde3`


  `python manage.py createsuperuser`

## Environment Variables


The project uses environment variables to store sensitive information. Follow the steps below to set up your environment:


1. Create a file named `.env` in the root directory of the project.

2. Copy the contents from `.env.sample` into `.env`.

3. Replace the values in `.env` with your actual environment variable values.


**Note:** Make sure not to commit your `.env` file to version control. It should be listed in the `.gitignore` file.