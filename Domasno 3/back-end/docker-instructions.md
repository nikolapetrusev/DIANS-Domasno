```
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic
docker compose exec web python manage.py createsuperuser
```