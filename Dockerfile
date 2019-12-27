FROM python:3.7.6

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

# CMD python manage.py runserver
CMD gunicorn gettingstarted.wsgi:application --bind 0.0.0.0:8000
