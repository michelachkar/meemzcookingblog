from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name:'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name:'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email:'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone:'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 5}))
    
    # Add a select box with options
    SERVICES_CHOICES = [
        ('general', 'General Inquiry'),
        ('support', 'Customer Support'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ]
    
    service = forms.ChoiceField(
        choices=SERVICES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
