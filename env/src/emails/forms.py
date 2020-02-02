from django import forms
from .models import Signup

class EmailSignUpForm(forms.ModelForm):
	#FORM FOR EMAIL COLLECTION
	email = forms.EmailField(label='',widget = forms.TextInput(attrs={
		"type":"email",
		"name": "email",
		"id": "email",
		"placeholder": "Type your email address",
		"class":"f6 f5-l input-reset bn fl black-80 bg-white pa3 lh-solid w-100 w-75-m w-80-l br2-ns br--left-ns",
		}))
	class Meta:
		model = Signup
		fields = ('email',)