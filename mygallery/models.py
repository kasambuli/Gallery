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
        return self.category

    def save_category(self):
        self.save()
    
    @classmethod
    def update_category(cls,id,new_category):
        cls.objects.filter(id).update(category = new_category)

    @classmethod
    def delete_category(cls,id):
        cls.objects.filter(id).delete()
    


class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_url = models.TextField(blank = True)
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

   
    class Meta:
        ordering = ['image_name'] 
        
    @classmethod
    def image_list(cls):
        
        images = cls.objects.all()
        return images

    @classmethod
    def get_photo_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images

   
    @classmethod
    def search_by_category(cls,searched_category):
        images = cls.objects.filter(image_category__category__icontains = searched_category)

        return images

    @classmethod
    def update_image(cls,id,new_image_name):
        cls.objects.filter(id=id).update(image_name =new_image_name)

    @classmethod
    def delete_location(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def Nairobi(cls):
        nairobi=cls.objects.filter(image_location__location='Nairobi')
        return nairobi

    @classmethod
    def Mombasa(cls):
        mombasa = cls.objects.filter(image_location__location='Mombasa')
        return mombasa
    @classmethod
    def Dubai(cls):
        dubai = cls.objects.filter(image_location__location='Dubai')
        return dubai