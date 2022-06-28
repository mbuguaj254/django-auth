from socket import fromshare
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import User_profile, Goal


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class setGoalsForm(ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"
        labels = {
            'user': '',
            'bsc': '',
            'total_bsc_weight': '',
            'strategic_initiative': '',
            'initiative_weight': '',
            'kpi': '',
            'target': ''
        }
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your username'}),
            'bsc': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your department BSC'}),
            'total_bsc_weight': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter BSC weight'}),
            'strategic_initiative': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter strategic initiative'}),
            'initiative_weight': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter initiative weight'}),
            'kpi': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter KPIs'}),
            'target': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your targets for KPI'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User_profile
        fields = "__all__" #Includes all fields but if only specific fields were required we use a tuple ()
        labels = {
            'staff_number':'',
            'first_name': '',
            'last_name': '',
            'job_title': '',
            'division': '',
            'department': '',
            'section': '',
            'station': '',
            'grade': '',
            'years_in_grade': '',
            'length_of_service': '',
            'evaluator': '',
            'duration_of_supervision': '',
            'assessment_period': ''

        }
        widgets = {
            'staff_number': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your staff number'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your last name'}),
            'job_title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your job title'}),
            'division': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your division'}),
            'department': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your department'}),
            'section': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your section'}),
            'station': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your station'}),
            'grade': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your staff job grade'}),
            'years_in_grade': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the number of years in current grade'}),
            'length_of_service': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter length of service in current grade'}),
            'evaluator': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Enter your evaluator's name"}),
            'duration_of_supervision': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the duration under your current evaluator '}),
            'assessment_period': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the assessment period'})
        }
