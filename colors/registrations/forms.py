from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    # email = forms.EmailField(
    #     max_length=100,
    #     widget=forms.TextInput({'class': 'form-control'}))
    # firstName = forms.CharField(max_length=50,
    #                             widget=forms.TextInput({'class': 'form-control'}))
    # lastName = forms.CharField(max_length=50,
    #                            widget=forms.TextInput({'class': 'form-control '}))
    # subject = forms.CharField(max_length=50,
    #                           widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Choose Option'}))
    # phoneNumber = forms.CharField(max_length=50,
    #                               widget=forms.TextInput({'class': 'form-control'}))
    # birthday = forms.DateField(
    #     widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control inputbackground'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control inputbackground'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control inputbackground'}),
            'subject': forms.Select(attrs={'class': 'form-control inputbackground'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control inputbackground'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control inputbackground'})
        }


