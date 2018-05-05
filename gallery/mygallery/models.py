from django.db import models

# Create your models here
class Location(models.Model):
    location = models.CharField(max_length =30)
   
    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
    
    
    @classmethod
    def update_location(cls,id,new_location):
        cls.objects.filter(id).update(location = new_location)

    @classmethod
    def delete_location(cls,id):
        cls.objects.filter(id).delete()

class Category(models.Model):
    category = models.CharField(max_length =30)
   
    def __str__(self):
        return self.location

    def save_category(self):
        self.save()
    
     @classmethod
    def update_category(cls,id,new_category):
        cls.objects.filter(id).update(location = new_category)

    @classmethod
    def delete_category(cls,id):
        cls.objects.filter(id).delete()
    


class Image(models.Model):
    image = models.CharField(max_length =30)
    image_url = models.TextField(blank = True)
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)


    def __str__(self):
        return self.location

    def save_image(self):
        self.save()

   
    class Meta:
        ordering = ['image_name']
    
    @classmethod
    def get_photo_by_id(cls,id):
        photos = cls.objects.get(id=id)
        return photos

    @classmethod
    def filter_photo_by_location(cls,image_location):
        photos = cls.objects.filter(image_location)
        return photos

    @classmethod
    def update_image(cls,id,new_image_name):
        cls.objects.filter(id=id).update(image_name =new_image_name)

    @classmethod
    def delete_location(cls,id):
        cls.objects.filter(id).delete()

       