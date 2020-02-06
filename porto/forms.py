from django import forms 
from . models import *



class ContactForm(forms.Form):
    """Model definition for ContactForm."""
    nom     = forms.CharField()
    email   = forms.EmailField(required=True)
    sujet   = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
