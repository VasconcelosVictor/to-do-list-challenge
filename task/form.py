from django import forms
from .models import *

class TimeRecordForm(forms.ModelForm):
    registration_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'text', 'placeholder': 'dia/mes/ano'}),
                           input_formats=['%d/%m/%Y'],  # Formato esperado para a entrada
    )

    class Meta:
        model = TimeRecord
        fields = ['description', 'minutes_worked', 'registration_date']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Digite a descrição', 'class': 'form-control'}),
            'minutes_worked': forms.NumberInput(attrs={'min': 0, 'placeholder': 'Minutos trabalhados', 'class': 'form-control'}),
        }


