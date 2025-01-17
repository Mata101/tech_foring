from django.test import TestCase,Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class TechForing(TestCase):
    def setUp(self):
        pass
    
    def register_user_test(self):
        c = Client()
        response = c.post(reverse('register_user'), data={'username': 'paul', 'email': 'paul@test.com','password':'samplepassword',
              'first_name':'Paul','last_name':'kwang'})
        print(response)
        self.assertTrue(status.is_success(response.status_code))