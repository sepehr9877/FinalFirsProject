from django import forms
from .models import User_Comments,Comments,Subscriber
class Add_comments(forms.Form):
    descriptions=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"enter your comments"}))
    def clean_descriptions(self):
        descriptions=self.cleaned_data.get("descriptions")
        return descriptions
class Subscriber_Comment(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields=('username','email','image')
    def clean_username(self):
        username=self.cleaned_data.get("username")
        existed_username=Subscriber.objects.filter(username=username)
        print(existed_username)
        if existed_username:
            raise forms.ValidationError("Choose another username")
        return username
    def clean_email(self):
        email=self.cleaned_data.get("email")
        existed_email=Subscriber.objects.filter(email=email)
        if existed_email:
            raise forms.ValidationError("This Email was choosen already")
        return email
class adding_comments(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your username"})
                             )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"Enter your Email"})
    )
    def clean_username(self):
        username=self.cleaned_data.get("username")
        return username
    def clean_email(self):
        email=self.cleaned_data.get("email")
        return email