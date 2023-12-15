from django import forms
from django.forms import widgets
from .models import status_choice, type_choice



class TaskForm(forms.Form):
    description = forms.CharField(max_length=255, label='Описание')
    detailed_description = forms.CharField(required=True, label='Детальное описание', widget=widgets.Textarea())
    status = forms.ChoiceField(choices=status_choice, label='Статус', required=False)
    type = forms.ChoiceField(choices=type_choice, label='Тип', required=False)
    data_of_complited = forms.DateTimeField(required=False)

# widget=widgets.HiddenInput()