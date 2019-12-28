# Python: Getting Started

A Salary Calculator in Taiwan, which can deploy to Google App Engine.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

```sh
$ python3 -m venv .venv

$ source .venv/bin/activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver
```

Your app should now be running on [localhost:8080](http://localhost:8080/).

## Deploying to Google App Engine

Update key in app.yaml

```yaml
TELEGRAM_TOKEN: "[TELEGRAM_TOKEN]"
SECRET_KEY: "[SECRET_KEY]"
```

Deploy to GAE

```sh
$ gcloud app create

$ gcloud app deploy
```

## Documentation

For more information about Google App Engine.

- [Python3 in GAE](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
