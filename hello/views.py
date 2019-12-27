import os
import logging
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import UpdateResponse

log = logging.getLogger(__name__)
token = os.environ.get('TOKEN', None)
# Create your views here.
def index(request):
    res = request.json()
    msg = res['message']
    return HttpResponse(msg)