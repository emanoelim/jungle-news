### Run application in development mode
* Install Docker Compose following the tutorial: https://docs.docker.com/compose/install/
* Build image: `docker-compose build`
* Start services: `docker-compose up -d`
* Run collectstatic: `docker-compose exec web python manage.py collectstatic --noinput`
* Run migrations: `docker-compose exec web python manage.py migrate`
* Create Django admin user: `docker-compose exec web python manage.py createsuperuser`
* Run tests: `docker-compose exec web coverage run --source='.' manage.py test`
* Coverage report: `docker-compose exec web coverage report`
* Url: http://0.0.0.0:8000/
