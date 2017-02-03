from django import forms


CATEGORIES = (  
    ('People', 'people'),
    ('Rooms', 'rooms'),
    ('Price', 'price'),
)


class ReviewForm(forms.Form):
	reviewTitle = forms.CharField(label='Title',widget=forms.TextInput(attrs={'class': "titleField"}))
	review = forms.CharField(label='Review Here', widget=forms.Textarea(attrs={'class': "reviewfield"}))
	propertyRating = forms.FloatField(min_value=0.0, max_value=5.0,
		label = 'Property Rating',widget=forms.TextInput(attrs={'class': "ratingField"}))
	landlordRating = forms.FloatField(min_value=0.0, max_value=5.0,
		label = 'Landlord Rating',widget=forms.TextInput(attrs={'class': "ratingField"}))

class LoginForm(forms.Form):
	username = forms.CharField(label = 'email')
	password = forms.CharField(label = 'password', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username = forms.CharField(label = 'email')
	password = forms.CharField(label = 'password', widget=forms.PasswordInput())

class SortForm(forms.Form):
	sortBy = forms.ChoiceField(label = 'Sort', choices=CATEGORIES )

