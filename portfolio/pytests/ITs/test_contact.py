from django.test import TestCase, Client
from django.urls import reverse

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("contact")

    def test_contact_view_status_code(self):
        """Teste si la vue contact retourne un code 200."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template_used(self):
        """Teste si la vue utilise le bon template."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "./portfolio/contact.html")
