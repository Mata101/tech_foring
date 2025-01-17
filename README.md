<h3>Installation</h3>
Download and Install Python: https://www.python.org/downloads/ \n
Create a virtual environment: python3 -m venv techforing_env \n
Activate python environment: source techforing_env/bin/activate \n
Install Django: https://docs.djangoproject.com/en/5.1/topics/install/ \n
Clone this repo: git clone https://github.com/Mata101/tech_foring.git \n
Install required python packages: cd [path_to_cloned_Repo] && pip install -r requirements.txt \n

<h3>Database setup</h3>
Note: this project only uses sqlite3 for this purpose
1. Activate your python environment.
2. Create migrations and migrate the database based on models initialized in models.py file.
  Run: python manage.py makemigrations && python manage.py migrate

<h3>Run the system</h3>
python manage.py runserver

<h3>API Documentation</h3>
https://documenter.getpostman.com/view/17373601/2sAYQakAj4
