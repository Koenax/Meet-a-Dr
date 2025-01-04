# DOWNLOAD AND SETUP DOCKER AND DOCKER COMPOSE
    - 

set up Django project (done)
    - set venv and activate: source myenv/bin/activate
    - run django server: python manage.py runserver
    - set up dockerfile and docker-composefile
        *docker-compose build
        *docker-compose up
        *docker-compose down
        *docker ps
        *docker exec -it new_project-web-1 /bin/bash

Connect django to postgres database (done)
   - docker exec -it postgres_db /bin/bash
   - psql -U postgres -h localhost -p 5432 -d meetadoctor_db

Create usermanager app
    - Create user models (done)
    - Created serializers (done)
    - Created superuser (done)

Create an app for registering doctor profiles
    - created doctor profile models (done)
    - Created serializers (done)

Create a patient profile and file management system
    - 

Errors
 - fix api/url/urls files