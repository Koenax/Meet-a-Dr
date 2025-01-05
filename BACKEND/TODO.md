# DOWNLOAD AND SETUP DOCKER AND DOCKER COMPOSE
    - create Dockerfile
    - create docker-compose file
    - Build the Docker image
        - docker-compose build
        - docker-compose logs db
        - docker-compose down -v

    - Start the containers:
        - docker-compose up
    - docker-compose up --build

# START DJANGO PROJECT
    - Start a Django project
        * django-admin startproject
    - Start a Django
        * django-admin startapp
        * docker-compose exec web python manage.py startapp
    - Migrate data to database
        * python manage.py makemigrations
        * python manage.py migrate
        * docker-compose exec web python manage.py makemigrations
        * docker-compose exec web python manage.py migrate

# git commit

# Apps
### Create usermanager app
    - Create user models
    - Created serializers
    - Created superuser
      * python manage.py createsuperuser
    - 
### Create an app for registering doctor profiles
    - created doctor profile models
    - Created serializers
    - created api views for the frontend
    - created urls file

### urls
localhost/api/doctors/
localhost/admin
localhost/