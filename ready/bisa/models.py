from django.db import models
from datetime import datetime
# Create your models here.

class ProductRekomen(models.Model):
    image = models.ImageField()
    nama = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama}"

class ProductElektronik(models.Model):
    image = models.ImageField()
    nama =  models.CharField(max_length=50)
    
    spek = models.CharField(max_length=20)
    
    harga = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama}"

class ProductOtomotif(models.Model):
    image = models.ImageField()
    nama =  models.CharField(max_length=50)
    
    spek = models.TextField()
    
    harga = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama}"


