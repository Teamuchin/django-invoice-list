from django.db import models

# Create your models here.
class FaturaList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.ForeignKey(FaturaList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    last_date = models.IntegerField(default=1,max_length=30)
    complete = models.BooleanField()
    def __str__(self):
        return self.text