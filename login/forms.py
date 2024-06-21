from django import forms

class LoginForm(forms.Form):
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