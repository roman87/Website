# Website

Requirements installation on Ubuntu

In terminal:

git clone https://github.com/roman87/Website.git

1. Installation of python pip3 intaller:

sudo apt-get update && apt-get upgrade -y

sudo apt-get install apt-utils -y

sudo apt-get install python3-pip -y

2. Installation of Flask:

sudo pip3 install flask

sudo pip3 install flask-wtf

sudo pip3 install flask-sqlalchemy

sudo pip3 install flask-migrate

3. PostgreSQL installation:

sudo apt-get install postgresql-9.5 postgresql-contrib-9.5 postgresql-client-9.5

4. Running postgres:

sudo servise postgresql start

5. Creation of database:

sudo -u postgres -i

psql

ALTER USER postgres WITH PASSWORD ‘postgres’;

CREATE DATABASE text;

\q

exit

6. Cheng working directory:

cd Website/webapp

7. Sett the FLASK_APP environment variable:

export FLASK_APP=microblog.py

8. Database initialization and creation of table:

flask db init

flask db migrate -m "my table"

flask db upgrade

9. Entering some text into the table (it must be some three articles in table):

flask shell

title = "some title"
article = "some article"
af = AF(title=title, article=article)
db.session.add(af)
db.session.commit()
exit()

10. Running web app:

flask run

11. Go to http://127.0.0.1:5000/
