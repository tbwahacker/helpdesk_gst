git rm -r --cached .
pip uninstall django-bootstrap-v5 django-bootstrap5 -y
pip install django-bootstrap5

cd Desktop
mkdir name of project
py -m venv venv

venv\Scripts\activate #activate
django-admin startproject name of project #start project

# install django
pip install django
django-admin startproject name
cd name -> enter project folder

# run server
py manage.py runserver

# how to push and pull
git init
git add .
git commit -m ""
git push origin ur branch
# click link to  merge

# pull
git pull origin ur branch

# how to migrate
py manage.py makemigrations