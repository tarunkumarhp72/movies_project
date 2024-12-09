# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput, label='email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Adding custom classes to the form fields
        self.fields['username'].widget.attrs.update({'class': 'form-control form_input','placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form_input','placeholder':'email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form_input','placeholder': 'password'})
        self.fields['confirm_password'].widget.attrs.update({'class': 'form-control form_input','placeholder':'confirm password'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
