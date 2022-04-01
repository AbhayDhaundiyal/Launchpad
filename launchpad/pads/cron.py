from .models import pads
from .serializers import padSerializer

def myjob():
  q = pads.objects.all()
  o = padSerializer(q, many = True).data
  for x in o :
    z = pads.objects.get(pk = x['pad_id'])
    z.active = False
    z.save()