from django import forms
from .models import PassWordManagerDataModel

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'JavascriptLover'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'monemail@test.fr'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'monpassword'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'JavascriptLover'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'monpassword'}))

class CreateNewSafeBox(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CreateNewSafeBox, self).__init__(*args, **kwargs)
    name = forms.CharField(label='Nom du coffre', max_length=100)

# class CreateNewCard(forms.ModelForm) :
#     class Meta: 
#         model = PassWordManagerDataModel
#         fields = ['websiteName', 'websiteUrl', 'password']

class CreateNewCard(forms.Form):
    websiteName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'mysite'}))
    websiteUrl = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder': 'http://mysite.fr'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'monpassword'}))
#Créer Ici un formulaire CreateNewCard en utilisant les champs définis dans le modèle PasswordManagerDataModel
    #AIDE
    # websiteName = models.CharField(max_length=100)
    # websiteUrl = models.URLField(blank=True, default='')
    # password = models.CharField(max_length=100)