from django.db import models

# Create your models here.
class Menu(models.Model):
    thali_name = models.CharField(max_length=200)
    kab_banaya = models.DateField('date published')

    def __str__(self):
        return self.thali_name

class kyakhayega(models.Model):
    thali = models.ForeignKey(Menu, on_delete=models.CASCADE)
    kitne_thali = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.kitne_thali