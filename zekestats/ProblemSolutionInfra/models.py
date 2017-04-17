from __future__ import unicode_literals

from django.db import models
from DataInventoryMgmt.models import DataSet
from django.template.defaultfilters import slugify
#from DataCratMgmt.models import Datacrat

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True,null=True)
    datasets = models.ManyToManyField(DataSet)
    photo = models.ImageField(upload_to='problems')
    slug = models.SlugField(blank=True,null=True,unique=True)
    
    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Problem, self).save()   
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
        
class Solution(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True,null=True)
    data = models.FileField(upload_to='solutions/%Y/%m/%d/')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    #datacrat = models.ForeignKey(Datacrat, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('title',)
