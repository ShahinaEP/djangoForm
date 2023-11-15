from django.db import models

# Create your models here.
class BannerSection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerImage')
    

    def __str__(self) :
        return str(self.id)
    

class ProductList(models.Model):
    name = models.CharField(max_length=255)
    short_des = models.TextField()
    image = models.ImageField(upload_to='ProductImage')
    

    def __str__(self) :
        return str(self.id)
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name + '/' + self.email

