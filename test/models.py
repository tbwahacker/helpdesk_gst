from django.db import models


class Test(models.Model):
    column1=models.TextField()
    column2=models.IntegerField(default=0)
    column3=models.CharField(unique=True, null=False)
    column4=models.DateField(auto_now=True)