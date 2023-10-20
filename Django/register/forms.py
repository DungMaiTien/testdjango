import email
import re
from cProfile import label

from django import forms
from django.contrib.auth.models import User
from django.contrib import messages


# class RegisterForm(forms.Form):
#     username = forms.CharField(label="Tai khoan", required=True)
#     email = forms.EmailField(label="Email")
#     password1 = forms.CharField(label="Mat Khau", widget=forms.PasswordInput,required=True)
#     password2 = forms.CharField(label="Xac nhan mat Khau", widget=forms.PasswordInput,required=True)
class RegisterForm(forms.Form):
    username = forms.CharField(label="Tai khoan", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Mat Khau", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(label="Xac nhan mat Khau", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    # Các phần còn lại của mã của bạn

    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
            raise forms.ValidationError("Mat khau khong hop le")
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', username):
            raise forms.ValidationError("Username khong hop le")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("user da ton tai")
    
    def save(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
            # is_staff = True,
        )
        
             
            
            
