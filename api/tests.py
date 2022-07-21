import json
from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status



# Create your tests here.
class CreateShortURL(APITestCase):

    def test_shortURL(self):
        data = { "original_link": "https://calendar.google.com/calendar/u/1/r",
          "shortened_link": "http://127.0.0.1:8000/Abc456"}
        
        response = self.client.post('/api/create/',data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)