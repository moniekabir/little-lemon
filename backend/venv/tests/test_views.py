from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title='Pizza', price=10.99, inventory=5)
        Menu.objects.create(title='Burger', price=8.99, inventory=3)
        Menu.objects.create(title='Salad', price=7.99, inventory=2)
        
    def test_get_all(self):
        # Create an API client
        client = APIClient()
        
        # Define the URL for retrieving all menu objects
        url = reverse('restaurant:menu')
        
        # Send a GET request to the URL
        response = client.get(url)
        
        # Retrieve all the Menu objects from the database
        menus = Menu.objects.all()
        
        # Serialize the Menu objects
        serializer = MenuSerializer(menus, many=True)
        
        # Assert that the serialized data matches the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)