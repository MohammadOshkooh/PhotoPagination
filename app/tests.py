from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Photo


class PhotoListAPITest(APITestCase):

    def setUp(self):
        for i in range(10):
            Photo.objects.create(photo=f'media/photo/{i}.jpg')

    def test_pagination(self):
        url = reverse('photo-list')
        response = self.client.get(url)

        # check Meta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(200, response.data['results']['Meta']['statusCode'])
        self.assertEqual('success', response.data['results']['Meta']['error'])

        # Test the number of items per page
        self.assertEqual(len(response.data['results']['Data']), 5)

        # Check values in pagination links
        self.assertEqual('http://testserver/photo/?page=2', response.data['next'])
        self.assertEqual(None, response.data['previous'])
        self.assertEqual(response.data['count'], 10)
