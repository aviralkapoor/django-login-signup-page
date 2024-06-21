from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(
		max_length=30,
		min_length=1,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "User Name",
				"class": "form-control"
			}
		)
	)
    #abc@xyz.com
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        )
    )
    #Password is already included from UserCreationForm
    """
    password = forms.CharField(
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )
    """
    dob = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        initial='M'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'dob', 'gender')