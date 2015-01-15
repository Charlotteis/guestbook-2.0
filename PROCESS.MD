### 15/01/2015
- Set up guestbook_2.0 virtualenv
- Check you have postgres installed (postgres.app)
- Ignore the ask to install Apache and mod_wsgi due to having no fucking clue
- Set up a guestbook postgres user and database using
    http://killtheyak.com/use-postgresql-with-django-flask/
- Installed django-toolbelt (Django, psycopg2 gunicorn, dj-database-url, dj-static)
  This allows us to work with Heroku (where, of course, this stuff will be hosted)
- Created the guestbook project with `django-admin.py startproject guestbook .`
  The period makes sure all the files are installed in the current directory
  rather than make a new subdirectory
- Set up Procfile for Heroku, launching django with Gunicorn
- Configured Settings for Heroku:
    - Static files in production
    - Database connection for Postgres
- Set SECRET_KEY as Environ Var
- Paranoidly check that I haven't left any secrets in
- Commit and Push to Repo
- Push to Heroku
- Add runtime.txt to force Heroku to use Python three
- Create guestbook2 application
- Create 'Post' model and Make Migrations
