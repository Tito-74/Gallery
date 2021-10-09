from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location

    # def save_location():
    #    self.save() 


class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category
    
    
    # def save_category():
    #    self.save() 

class Post(models.Model):
    name = models.CharField(max_length =60)
    desc = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    

    # f'{self.name} {self.desc}'
    
    # def save_post():
    #    self.save() 
