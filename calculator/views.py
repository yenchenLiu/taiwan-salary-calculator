import json
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
from calculator.util.formula import Salary

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        res = json.loads(request.body)
        message = res['message']
        chat = message['chat']
        salary = int(message['text'])
        s = Salary(salary)

        content = f"""
Hi {message['from']['username']}:
勞保費用:{s.get_total_labor()}
健保費用:{s.get_health_insurance()}
個人負擔小計:{s.get_total_labor() + s.get_health_insurance()}
實領薪資:{salary - (s.get_total_labor() + s.get_health_insurance())}
        """
        url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage?chat_id={chat["id"]}&text={content}'

        requests.get(url)

        return HttpResponse(res)
    else:
        raise Http404("Not Found")
