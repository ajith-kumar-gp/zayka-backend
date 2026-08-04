# project-food-del-backend


# Requirements

    python 3.11


# Run

Create virtual env

    py -m venv venv

navigate and activate virtual env

    .\venv\Scripts\activate 
     
flask= pip install flask

run  = flask run --debug --host <ipaddress:port>                

# to create requirements.txt file:
pip freeze > requirements.txt


## Note

Please use developement requirements----------

To install from requirements

    pip install -r "./requirements/development.txt"

To add packages to developement config

    pip freeze > ".\requirements\development.txt"    

To perform migrations use the appropiate commands to perform migrations

    flask db init --directory src/migrations             
    flask db migrate --directory src/migrations -m "migration message"
    flask db upgrade --directory src/migrations
    flask db downgrade --directory src/migrations








#SQLALCHEMY:-

# Step 1: Install SQLAlchemy
pip install SQLAlchemy

# Step 2: Install Flask-SQLAlchemy (Flask integration)
pip install Flask-SQLAlchemy

# Step 3: Install PostgreSQL driver for Python
pip install psycopg2-binary

# Optional: If you plan to use Flask-Migrate for DB migrations
pip install Flask-Migrate

