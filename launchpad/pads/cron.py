from .models import pads
from .serializers import padSerializer
from datetime import datetime

def myjob():
  q = pads.objects.all()
  o = padSerializer(q, many = True).data
  naive = datetime.now()
  now = naive.replace(tzinfo=None)
  for x in o :
    z = pads.objects.get(pk = x['pad_id'])
    if z.active == True :
      naive = z.active_since
      then = naive.replace(tzinfo = None)
      duration = now - then
      if duration.days >= 7:
        z.active = False
        z.save()