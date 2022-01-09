from django import forms 
from .models import ApplForJob , Job , Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = '__all__'



class AddJob(forms.ModelForm):
    class Meta:
        model = Job 
        fields = ['title' , 'image' , 'job_type' , 'descrption' , 'vacancy' , 'salary' , 'location' , 'experiance']




class ApplyJob(forms.ModelForm):
    class Meta:
        model = ApplForJob
        fields = '__all__'



class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Enter the username')
    password = forms.CharField(label='Enter the password' , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'password']



class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='password' , widget=forms.PasswordInput())
    password2 = forms.CharField(label='check the password password' , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']

