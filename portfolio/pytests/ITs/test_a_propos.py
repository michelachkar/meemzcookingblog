from django.test import TestCase, Client
from django.urls import reverse

class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("about")  # Assure-toi que le nom de l'URL est bien "about"

    def test_about_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "./portfolio/about.html")