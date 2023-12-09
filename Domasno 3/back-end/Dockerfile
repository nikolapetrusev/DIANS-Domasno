FROM python:3.10-slim

WORKDIR /code

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# COPY .env.dev /code
COPY . /code

# EXPOSE 8000

# RUN python project/manage.py runserver

# ENTRYPOINT ["python", "project/manage.py", "runserver"]
# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
