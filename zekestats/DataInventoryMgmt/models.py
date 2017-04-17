from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='category')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
    
class DataSet(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(blank=True,null=True,unique=True)
    categories = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to='datasets')
    data = models.FileField(upload_to='uploads/%Y/%m/%d/')
    downloads_count = models.IntegerField(blank=True,null=True)
    metadata = models.TextField(blank=True,null=True)
    
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(DataSet, self).save()    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        

    
 