from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class WeblogPageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/weblog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('weblog'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('weblog'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get('/weblog/')
        self.assertContains(response, '<h1>')