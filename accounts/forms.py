from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! Username and password maybe case-sensitive'

class SignupForm(UserCreationForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
        ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        ('School of Education', 'School of Education (SE)'),
        ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autofocus': True}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_no', 'school']


class UpdateProfileForm(forms.ModelForm):
    SELECT_YEAR_OF_STUDY = (
        (None, '-- Select year of study --'),
        ('First year', 'First year'),
        ('Sophomore', 'Sophomore'),
        ('Third year', 'Third year'),
        ('Fourth year', 'Fourth year')
    )

    class Meta:
        model = User
        fields = ['year', 'profile_pic']