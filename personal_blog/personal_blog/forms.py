from django import forms


class UserInformationForm(forms.Form):
    username = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserSignupForm(forms.Form):
    email = forms.EmailField(label='Email*')
    password = forms.CharField(label='Password*', widget=forms.PasswordInput)
    repeat_pass = forms.CharField(label='Repeat Password*', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name*')
    last_name = forms.CharField(label='Last Name*')
