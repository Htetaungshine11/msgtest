from django.db import models
from controls.models import Cuser




class group(models.Model):
    groupname=models.CharField(max_length=50,unique=True)
    user = models.ManyToManyField(Cuser,related_name="user")


class msg(models.Model):
    group = models.ForeignKey(group,on_delete=models.CASCADE,null=True)
    text = models.TextField()