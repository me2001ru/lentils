===============================
** -- Setting up the environment -- **

1) create venv and activate it.
- virtualenv venv (enter this in project directory)
- source venv/bin/activate
- add "venv" in .gitignore to avoid tracking file not related to the project.
  
2) now enter:
- pip install flask
- and confirm installation with : flask --version

3) import flask to main.py:
- from flask import Flask, render_template

====================

To run your web application, you’ll first tell Flask where to find the application with the FLASK_APP environment variable: export **export FLASK_APP=application/app**

Then run it in development mode with the FLASK_ENV environment variable:
export **FLASK_ENV=development**

then to run it: 
1) be in /Users/meru/Desktop/lentils
2) **export FLASK_APP=application/app** (if it can't / throws an error)
3) cmd: flask run

(IF you want to run *different* flask application to run at the same time, you must do it on a different port; cmd: flask run -p 5001)

==============
* create 'templates folder in the application folder'

* created base.html - as template file, which other html files can inherit.
In this file, Bootstraptoolkit is also used.

* add index.html file inside templates folder, inherited base.html with some modifications.

==============
** -- In the next step, you’ll set up a database that will store your application data. -- **

[[
    You’ll use a **SQLite database file** to store your data because the sqlite3 module, which we will use to interact with the database, is readily available in the standard Python library. For more information about SQLite, check out this tutorial.
]]
create sql.schema:
* touch schem.sql in root folder.

Now that you have a SQL schema in the schema.sql file, you’ll use it to create the database using a Python file that will generate an SQLite .db database file.
* touch init_db.py in root folder.

in 'app.py' add database connection and return it:

def get_db_connection():
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
return conn

[[
    This get_db_connection() function opens a connection to the database.db database file, and then sets the row_factory attribute to sqlite3.Row so you can have name-based access to columns. This means that the database connection will return rows that behave like regular Python dictionaries. Lastly, the function returns the conn connection object you’ll be using to access the database.
]]

** -- Displaying a Single Post -- **
from werkzeug.exceptions import abort

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

