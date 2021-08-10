
from django import forms
from .models import Contact
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    #phone = forms.CharField(required=True)
    email_from = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
class ContactFormDb(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','email_from','subject','message',)