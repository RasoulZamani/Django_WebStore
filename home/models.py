from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub       = models.BooleanField(default=False)
    
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse("home:category_filter", args=[self.slug,])
    
        
    def __str__(self) -> str:
        return self.name
        
class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d')#create folders based on date and store uploaded image to them
    description = RichTextField()
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
    
    