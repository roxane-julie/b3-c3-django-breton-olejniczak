from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'JavascriptLover'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'monemail@test.fr'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'monpassword'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'JavascriptLover'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'monpassword'}))