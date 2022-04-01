from django.db import models

class pads(models.Model):
    pad_id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length= 20, default="None")
    active = models.BooleanField(default = True)
    active_since = models.DateTimeField()

    def __str__(self):
        return self.owner