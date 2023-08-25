from django.db import models
from datetime import datetime
from accounts.models import Users


class Mymessages(models.Model):
   agent_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING, default='0')
   name= models.CharField(max_length=225)
   email= models.CharField(max_length=225)
   phone= models.CharField(max_length=225)
   comment= models.TextField()
   pname= models.CharField(max_length=225)
   plocation= models.CharField(max_length=225)
   msg_date= models.DateTimeField(auto_now_add=True, blank=True)

   def __str__(self):
      return self.name
