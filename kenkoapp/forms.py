from django import forms
from django.contrib.auth.models import User
from kenkoapp.models import Carepro, Care

# this is where your form question will be defined for your user
class UserForm(forms.ModelForm):
	email = forms.CharField(max_length=100, required=True)
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')

# this is where your form question will be defined for your user
class UserFormForEdit(forms.ModelForm):
	email = forms.CharField(max_length=100, required=True)
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')		

# this is where your form question will be defined for your carepro
class CareproForm(forms.ModelForm):
	class Meta:
		model = Carepro
		fields = ('name', 'number', 'address', 'avatar')

class CareForm(forms.ModelForm):
	class Meta:
		model = Care
		exclude = ('carepro',)	

