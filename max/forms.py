from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo  # import UserProfileInfo model

# Create a form for UserForm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())  # datatype of the password field
    class Meta():
        model = User # name of the model where it stores the data posted on the form
        fields = ('username','password','email') # field of the form

# Create a form for UserProfileInfo form
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo  # name of the model where it stores the data posted on the form
         fields = ('mobile_no', 'address') # field of the form
