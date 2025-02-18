inicializace: docker compose run web django-admin startproject config .


docker compose up --build
docker compose run web python manage.py migrate


docker compose run web python manage.py startapp api

docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate


lokálně:

python manage.py migrate

python manage.py runserver

python manage.py makemigrations api
python manage.py migrate
