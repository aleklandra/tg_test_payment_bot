from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = (
            'external_id',
            'first_name',
            'last_name',
            'username'
        )
        widgets = {
            'first_name': forms.TextInput,
            'last_name': forms.TextInput,
            'username': forms.TextInput,
        }
