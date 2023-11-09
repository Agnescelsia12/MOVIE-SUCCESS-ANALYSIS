from django.db import models

class Movie(models.Model):
    fname=models.CharField( max_length=50)
    aname=models.CharField( max_length=50)
    aaname=models.CharField( max_length=50)
    amt=models.CharField( max_length=50)   
    camt=models.CharField( max_length=50)
    happy=models.CharField( max_length=50)
    sad=models.CharField( max_length=50)
    tot=models.CharField( max_length=50)
    
    