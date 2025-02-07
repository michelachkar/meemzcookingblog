from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from portfolio.forms.contact_form import ContactForm
from unittest.mock import patch

class ContactFormViewTest(TestCase):

    def setUp(self):
        # Set up any necessary data for the test
        self.url = reverse('contact')  # Replace with the correct URL name for the form view

    def test_form_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './portfolio/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    @patch('portfolio.views.send_mail')  # Mock the send_mail function to not actually send emails during testing
    def test_form_view_post_valid_data(self, mock_send_mail):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        response = self.client.post(self.url, form_data)

        # Check if email is sent
        mock_send_mail.assert_called_once()
        subject = f"Message from John Doe"
        body = "Name: John Doe\nEmail: john.doe@example.com\nPhone: 1234567890\n\nMessage:\nThis is a test message."
        mock_send_mail.assert_called_with(subject, body, settings.DEFAULT_FROM_EMAIL, ['meeriamzouein@gmail.com'])

        # Check the redirect after form submission
        self.assertRedirects(response, '/')

    def test_form_view_post_invalid_data(self):
        # Simulate invalid form data
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'invalid_email',
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        response = self.client.post(self.url, form_data)

        # Ensure the form is present in the context
        form = response.context['form']

        # Check if the form is not valid
        self.assertFalse(form.is_valid())

        # Check for specific form errors
        self.assertIn('first_name', form.errors)
        self.assertIn('email', form.errors)

        # Check the specific error messages
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

        # Ensure the status code is 200 (page is rendered with errors)
        self.assertEqual(response.status_code, 200)

    @patch('portfolio.views.send_mail')  # Mock the send_mail function
    def test_form_view_sends_email_on_valid_submission(self, mock_send_mail):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'phone': '0987654321',
            'message': 'Another test message.'
        }
        response = self.client.post(self.url, form_data)

        # Verify the email was sent
        mock_send_mail.assert_called_once()
        subject = f"Message from Jane Doe"
        body = "Name: Jane Doe\nEmail: jane.doe@example.com\nPhone: 0987654321\n\nMessage:\nAnother test message."
        mock_send_mail.assert_called_with(subject, body, settings.DEFAULT_FROM_EMAIL, ['meeriamzouein@gmail.com'])

        # Ensure the user is redirected to the success page
        self.assertRedirects(response, '/')

    def test_form_view_post_missing_required_fields(self):
        # Simulate missing required fields
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': 'missing.fields@example.com',
            'phone': '1234567890',
            'message': ''
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid
        form = response.context['form']
        self.assertFalse(form.is_valid())

        # Check for missing required field errors
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('message', form.errors)

        # Ensure status code is 200
        self.assertEqual(response.status_code, 200)

    def test_form_view_post_email_with_invalid_format(self):
        # Invalid email format
        form_data = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'invalid-email',  # Invalid email format
            'phone': '9876543210',
            'message': 'Message with invalid email.'
        }
        response = self.client.post(self.url, form_data)

        # Ensure form is invalid
        form = response.context['form']
        self.assertFalse(form.is_valid())

        # Check email field error
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

        # Ensure status code is 200
        self.assertEqual(response.status_code, 200)
