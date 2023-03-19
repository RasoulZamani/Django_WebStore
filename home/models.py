from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self) -> str:
        return self.name
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d')#create folders based on date and store uploaded image to them
    description = models.TextField()
    available = models.BooleanField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("home:product_detail", args=[self.slug])
    
    