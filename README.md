# CollectiveProviderGuide

An application for discovering health care providers.

This was created as part of my volunteering efforts to support non profit organizations aimed at providing resources and education to help people find health care providers.

* [The Black Girl Health Collective](https://www.blackgirlhealthcollective.org/)
* [The Healthcare Navigation Project](https://thehealthcarenavigationproject.org/)

I think I want to evolve using Django as backend and Vue.js as frontend, with graphql in front of rest API. But this is a lot of complexity and learning curve too. So starting with just Django and templates for now.

Need to learn how to create data model and edit data.

## Setting Up The Backend Project
poetry add django@latest djangorestframework@latest psycopg@latest

poetry run django-admin startproject provider_guide .

edit settings.py
    * configure allow host
    * move secret key to local_settings.py
    * enable postgresql backend in local_settings.py

setup databae
```psql
create user collective password 'xxxxxx';
create schema collective authorization collective;
```
poetry run python manage.py migrate
poetry run python manage.py createsuperuser

poetry run python manage.py runserver 0.0.0.0:8000

poetry run python manage.py makemigrations
poetry run python manage.py migrate

### Specific applications

poetry run python manage.py startapp bghc

poetry run python manage.py startapp thcnp

poetry run python manage.py startapp directory

## Frontend Project

https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/

npm install -g vue-cli

vue init webpack frontend

* edit config/index.js. change host
* edit build/webpack.dev.config.js, add allowedHosts

webpack doesnt understand ipv6. i should disable this since i don't even use it.
but work around export HOST=192.168.10.11 and then try to run

npm run dev
