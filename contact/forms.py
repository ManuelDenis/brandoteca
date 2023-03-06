from django import forms
from contact.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
