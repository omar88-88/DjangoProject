from django import forms
from .models import Person
from multiselectfield import MultiSelectField


class UserRegister(forms.Form):
	first_name  = forms.CharField(required= True, widget= forms.TextInput())
	last_name   = forms.CharField(required= True, widget= forms.TextInput())
	tlf         = forms.CharField(required= True, widget= forms.TextInput())
	e_post      = forms.CharField(required= True, widget= forms.TextInput())

	date_test1  = forms.DateTimeField()
	


class Time_Test(forms.Form):
	BY_DEL_CHOICES = [
		('fjell', 'Fjell'),
		('sund', 'Sund'),
		('oygarden', 'Øygarden'),
	]
	title        = forms.CharField(required=True)
	date_test    = forms.DateTimeField()
	bydel = MultiSelectField(choices=BY_DEL_CHOICES)
	ham = forms.CharField(max_length=30)


