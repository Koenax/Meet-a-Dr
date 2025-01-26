# Use the official Python image
FROM python:3.13-slim

# Set the working directory
WORKDIR /djangobackend

# prevents Python from writing .pyc files (compiled bytecode files)
ENV PYTHONDONTWRITEBYTECODE 1

#Ensures that output is displayed immediately without buffering
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd


# Install the dependencies from the requirements.txt
RUN pip install --upgrade pip

# Copy the requirements.txt into the container
COPY requirements.txt /djangobackend/

COPY ./entrypoint.sh /djangobackend/

RUN sed -i 's/\r$//g' /djangobackend/entrypoint.sh
RUN chmod u+x /djangobackend/entrypoint.sh

# Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /djangobackend/
# Sets the entry point to the entrypoint.sh script and runs the Django development server.
ENTRYPOINT [ "/djangobackend/entrypoint.sh" ]

# Expose the port that the app will run on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
