from django import forms
from contact.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your message here...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'})
        }
