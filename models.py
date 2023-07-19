from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User , on_delete = models.SET_NULL , null = True , blank = True)
    notesdata = models.TextField()
    # idename = models.IntegerField()
    

    def __str__(self):
        return self.notesdata