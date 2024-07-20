# CollectiveProviderGuide


## Setting Up Project

poetry run django-admin startproject provider_guide .

edit settings.py

poetry run python manage.py migrate
poetry run python manage.py createsuperuser

poetry run python manage.py runserver 0.0.0.0:8000

poetry run python manage.py makemigrations
poetry run python manage.py migrate