from django.forms import ModelForm
from .models import AdditionalData


class IndexForm(ModelForm):
    class Meta:
        model = AdditionalData
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
            'email': 'Електронна Пошта',
        }
