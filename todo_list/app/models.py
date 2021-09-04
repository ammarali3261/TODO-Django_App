from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=100) 
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        
    def __str__(self):
        return self.name 

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,default="general",) 
    
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    
    choices = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    
    priority = models.CharField(max_length=6,choices=choices,default=HIGH,)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'