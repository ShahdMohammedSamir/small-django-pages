from django import forms
from .models import Login

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         max_length=100, 
#         label='Username',
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput,
#         label='Password',
#         required=True
#     )

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'username': 'Your Username',
            'password': 'Your Password'
        }