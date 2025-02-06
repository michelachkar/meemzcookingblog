from django.test import TestCase
from django.urls import reverse

class ServiceDetailTests(TestCase):
    # Test that valid service slugs return a 200 response and the correct template
    def test_valid_service_detail_views(self):
            valid_slugs = [
                'cours-de-cuisine',
                'team-building-cuisine',
                'atelier-cuisine-enfants'
            ]
            
            for slug in valid_slugs:
                response = self.client.get(reverse('service_detail', args=[slug]))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, f"portfolio/services/service_{slug.replace('-', '_')}.html")
        
    # Test that an invalid service slug returns a 404 response
    def test_invalid_service_detail_view(self):
            response = self.client.get(reverse('service_detail', args=['invalid-slug']))
            self.assertEqual(response.status_code, 404)
