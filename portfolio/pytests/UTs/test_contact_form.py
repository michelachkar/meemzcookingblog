from django.test import TestCase
from portfolio.forms.contact_form import ContactForm

class ContactFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'service': 'support',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        # Missing email
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'service': 'support',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_phone_length(self):
        # Phone number exceeds max length
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890123456',  # Exceeds 15 characters
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_form_invalid_email(self):
        # Invalid email format
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@com',  # Invalid email
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_missing_first_name(self):
        # Missing first name
        form_data = {
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_form_missing_message(self):
        # Missing message
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)


    def test_form_valid_phone(self):
        # Valid phone number
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',  # Valid phone
            'service': 'support',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
