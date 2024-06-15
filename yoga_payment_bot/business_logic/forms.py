from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = (
            'external_id',
            'name'
        )
        widgets = {
            'name': forms.TextInput
        }
