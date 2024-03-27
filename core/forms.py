from django import forms
from .models import Messages


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['email', 'message']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'email', 'autofocus': False}),
            'message': forms.Textarea(attrs={'class': 'message', 'placeholder': 'message', 'autofocus': False})
        }

        labels = {'Email': 'Email Address', 'message': 'message'}







    # email = forms.EmailField(
    #     label="Email Address", widget=forms.EmailInput(attrs={'class': "email", "placeholder": "email"})
    # )
    # message = forms.CharField(
    #     required=False, label="message", max_length=5000,
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'message',
    #             'placeholder': 'message'
    #                }
    #     ),
    #
    # )
    #
    #
