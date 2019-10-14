from django.test import TestCase
from .models import Category,Image,Location
# Create your tests here.


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.social= Category(category_name = 'Social')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.social,Category))

    # Testing Save Method
    def test_save_method(self):
        self.social.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(location_name = 'Kigali')

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

     # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


class ImageTestClass(TestCase):

    def setUp(self):
        # choosing a new category and saving it
        self.social= Category(category_name = 'Social')
        self.social.save_category()

        # inputing a location and saving it
        self.new_location = Location(location_name = 'Kigali')
        self.new_location.save()

        self.new_image= Image(image_name = 'Test Article',image_description = 'This is a random test Post',category = self.social)
        self.new_image.save()

        self.new_image.Location.add(self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    