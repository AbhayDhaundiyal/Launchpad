from django.http import HttpResponse
import simplejson as json

def hello(request):
    if request.method == 'GET':
        return HttpResponse("Hello")