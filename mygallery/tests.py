from django.test import TestCase
from .models import Location,Image,Category
# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_location= Location(location = 'Nairobi')

    def update_location(self):
        self.new_location.save_location()
        location_id = self.new_location.id
        Location.update_location(id,"mombasa")
        self.assertEqual(self.new_location.location,"mombasa")
        
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_category= Category(category = 'travel')

    def update_category(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(id,"travel")
        self.assertEqual(self.category.category,"travel")
        
class ImageTestClass(TestCase):
    #location
    def setUp(self):
        self.new_location= Location(location = 'Nairobi')

    #category
    def setUp(self):
        self.new_category= Category(category = 'travel')

    # Set up method
    def setUp(self):
        self.new_image= Image(image = 'image1.jpg',image_url = 'http://wallpaperstone.blogspot.com/2007/09/view-wallpaper-in-room.html',image_name = 'purple',image_description = 'purple table',image_location = 'Nairobi',image_category = 'travel')

    def test_save_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def update_image(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(id,"image1.jpg","purple table")
        self.assertEqual(self.category.category,"image1.jpg","purple table")
        
   