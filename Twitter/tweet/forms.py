from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TweetForm(forms.ModelForm):
  class Meta:                      # coding standard 
    model = Tweet                  # define the name of the model that you will using 
    fields = ['text', 'photo']     # Array type - define the feild of that model you will using from model
    

        
class UserRegistrationForm(UserCreationForm):      # Django in-built form
   email = forms.EmailField() 
   class Meta:
     model = User
     fields = ( 'username' , 'email' , 'password1' , 'password2')              # We are using built-in forms hence tuple / While mentioning password1 , password2 all Django in-bulit security features are enabled