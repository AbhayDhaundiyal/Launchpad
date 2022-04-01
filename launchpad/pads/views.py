from django.http import HttpResponse
import simplejson as json
from .models import pads
from .serializers import padSerializer

def hello(request):
    if request.method == 'GET':
        q = pads.objects.all()
        print(q)
        o = padSerializer(q, many = True).data
        for x in o :
            z = pads.objects.get(pk = x['pad_id'])
            z.active = False
            z.save()
        return HttpResponse("Hello")