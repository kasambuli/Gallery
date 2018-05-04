from django.db import models

# Create your models here
class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
    
    def update_location(self):
        self.update()

    def delete_editor(self):
        self.delete()
    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_category(self):
        self.save()
    
    def update_category(self):
        self.update()

    def delete_category(self):
        self.delete()
    class Meta:
        ordering = ['location']

class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.CharField(max_length =30)
    image_category = models.CharField(max_length =30)


    def __str__(self):
        return self.location

    def save_image(self):
        self.save()
    
    def update_image(self):
        self.update()

    def delete_image(self):
        self.delete()
    class Meta:
        ordering = ['location']