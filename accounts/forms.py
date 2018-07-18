from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from dateutil import relativedelta
import calendar,datetime

from .models import User


YEARS = range(datetime.datetime.now().year,1897,-1)


class UserRegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control mt-4','placeholder':'First name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control mt-4','placeholder':'Last name'}))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control mt-4','placeholder':'Password'}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control mt-4','placeholder':'Confirm password'}))    

    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS,attrs={'class':'form-control col-md-3 mr-2 mt-4',}))

    class Meta:
        model = User
        fields = ('email','password','first_name','last_name','birth_date',)

    def clean_birth_date(self):
        """ Validate birth_date here
        """
        birthdate = self.cleaned_data.get('birth_date')
        current_date = datetime.datetime.now()

        difference = relativedelta.relativedelta(current_date.date(), birthdate)

        if difference.years and difference.years >= 18:
            return birthdate
        else:
            raise forms.ValidationError('To sign up, you must be 18 or older.')

    def clean_confirm_password(self):
        """ Validate password 
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password did not match.')

        return confirm_password

    def save(self,commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        
        if commit:
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')

            instance.set_password(password)
            instance.save()
            return instance


class LoginForm(forms.Form):

    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput)

    def clean(self):
        """ Validate email address and password
        """
        user = None
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Invalid credentials. Please try again.')
        else:
            self.user = user

class ResetPasswordForm(forms.Form):
    """ Reset Password Form
    """
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and not User.get_object_or_404(email=email):
            raise forms.ValidationError('Email registration not detected.')

        return email
