Pasos a Ejecutar en caso de levantar la aplicación desde 0.

docker-compose up --build

docker-compose run django_app python app/manage.py migrate

docker-compose run django_app python app/manage.py collectstatic

docker-compose run django_app python app/manage.py createsuperuser

El usuario actual es:
User: Admin1
Password: 7410
