from django.db import models


class Fruits(models.Model):
    name = models.CharField(max_length=50)
    descript = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)
