# CollectiveProviderGuide

An application for discovering health care providers.

This was created as part of my volunteering efforts to support non profit organizations aimed at providing resources and education to help people find health care providers.

* [The Black Girl Health Collective](https://www.blackgirlhealthcollective.org/)
* [The Healthcare Navigation Project](https://thehealthcarenavigationproject.org/)

## Setting Up Project

poetry run django-admin startproject provider_guide .

edit settings.py
    * configure allow host
    * move secret key to local_settings.py

poetry run python manage.py migrate
poetry run python manage.py createsuperuser

poetry run python manage.py runserver 0.0.0.0:8000

poetry run python manage.py makemigrations
poetry run python manage.py migrate

## Specific backends

poetry run python manage.py startapp bghc
