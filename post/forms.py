from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('id','title', 'content', 'image') 
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
        }       
        

class SignupForm(UserCreationForm):
  
    # first_name = forms.CharField(max_length=50, required=False,help_text='optional')
    # last_name = forms.CharField(max_length=50, required=False,help_text='optional')
    # email = forms.EmailField(max_length=50, required=False,help_text='optional')   
    

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }