from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile
class Image_user_Form(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image_user']

class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Enter your name"})
        , label="username"
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"enter your password"})
        ,label="password"
    )

    def clean_username(self):
        username=self.cleaned_data.get("username")
        existed_user=User.objects.filter(username=username)
        if not existed_user:
            raise forms.ValidationError("there is no such a user")
        return username
    def clean_password(self):
        username=self.cleaned_data.get("username")
        print(username)
        password=self.cleaned_data.get("password")
        print(password)
        existed_user=authenticate(username=username,password=password)
        print(existed_user)
        if not existed_user:
            raise forms.ValidationError("The password is Wrong")
        return password
class Registerform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Enter your name"})
        ,label="username"
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"Enter your email"})
        ,label="Email"
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
        ,label="password"
    )
    repassword=forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password again"})
        ,label="repassword"
    )
    def clean_username(self):
        username=self.cleaned_data.get("username")
        isExisteduser=User.objects.filter(username=username)
        if isExisteduser:
            raise forms.ValidationError("choose another username")
        print(username)
        return username
    # def clean_email(self):
    #     email=self.cleaned_data.get("email")
    #     return email
    def clean_repassword(self):
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")
        print(repassword)
        if password != repassword:
            raise forms.ValidationError("Passwords are conflicted")
        print(password)
        return repassword
