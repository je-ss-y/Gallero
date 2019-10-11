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

