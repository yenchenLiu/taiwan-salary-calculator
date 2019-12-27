import os
import logging
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

log = logging.getLogger(__name__)
token = os.environ.get('TOKEN', None)
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        res = json.loads(request.body)
        msg = res['message']
        return HttpResponse(msg)
    else:
        raise Http404("Not Found")
