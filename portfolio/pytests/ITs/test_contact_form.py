from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from portfolio.forms.contact_form import ContactForm
from unittest.mock import patch

class ContactFormViewTest(TestCase):

    def setUp(self):
        # Set up necessary URL for the form view
        self.url = reverse('contact')  # Replace with the correct URL name for the form view

    def test_form_view_get(self):
        # Test for GET request, ensuring form is loaded correctly
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './portfolio/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    @patch('portfolio.views.send_mail')  # Mock the send_mail function to prevent actual email sending
    def test_form_view_post_valid_data(self, mock_send_mail):
        # Test POST with valid data and verify the email sending
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'service': 'general',  # Ensure valid service choice
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        response = self.client.post(self.url, form_data)

        # Ensure email was sent with correct data
        mock_send_mail.assert_called_once_with(
            f"Message from John Doe", 
            "Name: John Doe\nEmail: john.doe@example.com\nPhone: 1234567890\n\nService: general\n\nMessage:\nThis is a test message.",
            settings.DEFAULT_FROM_EMAIL, 
            ['meeriamzouein@gmail.com']
        )

        # Ensure the user is redirected after successful form submission
        self.assertRedirects(response, '/')

    @patch('portfolio.views.send_mail')  # Mock the send_mail function
    def test_form_view_post_invalid_data(self, mock_send_mail):
        # Test POST with invalid data (missing required fields, invalid email)
        form_data = {
            'first_name': '',  # Missing first name
            'last_name': 'Doe',
            'email': 'invalid_email',  # Invalid email format
            'service': 'general', 
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid and appropriate errors are shown
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

        # Check if the page is rendered again with the form errors
        self.assertEqual(response.status_code, 200)

    @patch('portfolio.views.send_mail')  # Mock the send_mail function
    def test_form_view_sends_email_on_valid_submission(self, mock_send_mail):
        # Test POST with valid data and check email sending
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'phone': '0987654321',
            'message': 'Another test message.',
            'service': 'support'
        }
        response = self.client.post(self.url, form_data)

        # Verify the email was sent with correct data
        mock_send_mail.assert_called_once_with(
            f"Message from Jane Doe", 
            "Name: Jane Doe\nEmail: jane.doe@example.com\nPhone: 0987654321\n\nService: support\n\nMessage:\nAnother test message.",
            settings.DEFAULT_FROM_EMAIL, 
            ['meeriamzouein@gmail.com']
        )

        # Ensure the user is redirected after form submission
        self.assertRedirects(response, '/')

    def test_form_view_post_missing_required_fields(self):
        # Test POST with missing required fields
        form_data = {
            'first_name': '',  # Missing first name
            'last_name': '',  # Missing last name
            'email': 'missing.fields@example.com',
            'phone': '1234567890',
            'message': ''  # Missing message
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid and appropriate errors are shown
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('message', form.errors)

        # Check that the page renders with status code 200
        self.assertEqual(response.status_code, 200)

    def test_form_view_post_invalid_email_format(self):
        # Test POST with invalid email format
        form_data = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'invalid-email',  # Invalid email format
            'phone': '9876543210',
            'message': 'Message with invalid email.',
            'service': 'feedback'
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid and appropriate errors are shown
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

        # Ensure page is rendered again with errors and status code 200
        self.assertEqual(response.status_code, 200)

    def test_form_view_post_invalid_service_choice(self):
        # Test POST with an invalid service choice (not in the predefined options)
        form_data = {
            'first_name': 'Invalid',
            'last_name': 'Choice',
            'email': 'invalid.choice@example.com',
            'phone': '1234567890',
            'message': 'Message with invalid service choice.',
            'service': 'nonexistent'  # Invalid service option
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid due to invalid service choice
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('service', form.errors)

        # Ensure the page renders again with the errors
        self.assertEqual(response.status_code, 200)
