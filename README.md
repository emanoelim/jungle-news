### Development mode
* Create a .env file:
```
SECRET_KEY=your_secret_key
DEBUG=1
DATABASE_HOST=db
USE_S3=0
```
* If you want to use your S3 bucket to upload images, chnage `USE_S3=1` and add:
```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_access_key_secret
AWS_STORAGE_BUCKET_NAME=your_buckt_name
```
* Install Docker Compose following the tutorial: https://docs.docker.com/compose/install/
* Build image: `docker-compose build`
* Start services: `docker-compose up -d`
* Run collectstatic: `docker-compose exec web python manage.py collectstatic --noinput`
* Run migrations: `docker-compose exec web python manage.py migrate`
* Run tests: `docker-compose exec web coverage run --source='.' manage.py test`
* Coverage report: `docker-compose exec web coverage report`
* Create Django admin user: `docker-compose exec web python manage.py createsuperuser`
* Url: http://0.0.0.0:8000/

### Production mode
* The application is running on Heroku. Deploy is done automatically after a merge to the `master` branch.

### Documentation
* https://jungle-news.herokuapp.com/api/swagger
