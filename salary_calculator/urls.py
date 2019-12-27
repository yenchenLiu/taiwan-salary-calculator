from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path(f"{settings.TELEGRAM_TOKEN}", include("calculator.urls"))
]
