from django import forms

class ReviewForm(forms.Form):
	reviewTitle = forms.CharField(label='Title')
	review = forms.CharField(label='Review Here')
	propertyRating = forms.FloatField()
	landlordRating = forms.FloatField()

class LoginForm(forms.Form):
	username = forms.CharField(label = 'email')
	password = forms.CharField(label = 'password', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username = forms.CharField(label = 'email')
	password = forms.CharField(label = 'password', widget=forms.PasswordInput())

