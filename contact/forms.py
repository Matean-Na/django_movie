from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "Enter your email..."})
        }
        labels = {
            "email": ""
        }
