from django.http import HttpResponse
import simplejson as json
from .models import pads
from .serializers import padSerializer
from datetime import datetime
from rest_framework.renderers import JSONRenderer

def show(request):
    if request.method == 'GET':
        query = pads.objects.all()
        data = padSerializer(query, many = True)
        # print(data.data)
        jsondata = JSONRenderer().render(data.data)
        print(jsondata)
        # return HttpResponse("G")
        return HttpResponse(jsondata)

def show_one(request, id):
    if request.method == 'GET':
        query = pads.objects.get(pk = id)
        data = padSerializer(query)
        jsondata = JSONRenderer().render(data.data)
        print(jsondata)
        return HttpResponse(jsondata)

def book(request, id, days):
    if request.method == 'GET':
        query = pads.objects.get(pk = id)
        if query.active == True:
            query.active = False
            query.active_since = datetime.now()
            query.For = days
            query.save()
            return HttpResponse("Sucess")
        else:
            return HttpResponse("The Pad Is Taken")