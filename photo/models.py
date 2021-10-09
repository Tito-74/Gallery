from django.db import models

# Create your models here.

class Location():
    location = models.CharField(max_length =30)
    def__str__(self):
        return self.location


class Category():
    category = models.CharField(max_length =30)
    def__str__(self):
        return self.category

class Post():
    name = models.CharField(max_length =60)
    desc = models.TextField()
    category = models.ForeignKey(category)
    location = models.ForeignKey(location)
    def__str__(self):
        return f'{self.name} {self.desc}'
    
    
