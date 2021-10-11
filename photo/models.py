from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location

    def delete_location():
        self.delete()

    @classmethod
    def get_locations(cls):
        location = Location.objects.all()
        return location
    


class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category
    
    
    def save_category():
        self.save()

        

    def delete_category():
        self.delete()
        

class Post(models.Model):
    name = models.CharField(max_length =60)
    desc = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'posts/')

    def __str__(self):
        return self.name
    # f'{self.name} {self.desc}'
    
    
    def save_post():
        self.save() 


    def delete_post():
        self.delete()

    @classmethod
    def update_post(cls, id,post):
        cls.objects.filter(id=id).update(post=post)
    @classmethod
    def search_category(cls,category):
        image =cls.objects.filter(category__category__icontains=category)
        return image
    
    @classmethod
    def get_post_by_id(cls, post_id):
        image = cls.objects.get(id=post_id)
        return image
 



       
