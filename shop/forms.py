from django import forms

class loginForm(forms.Form):
	username = forms.CharField(max_length = 16, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder':'Enter Your Name'
		}))
	password = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs= {
		'class':'form-control', 'placeholder':'Enter Your Password'
		}))

class signupForm(forms.Form):
	username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder':'Enter Your Name'
		}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder':'Enter Your Email'
		}))
	password = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder':'Enter Your Password'
		}))
	re_password = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder':'Retype Your Password'
		}))