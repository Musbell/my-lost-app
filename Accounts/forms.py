from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import Profile

class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = (
            'state',
            'local_government',
            'nationality',
            'occupation',
            'gender',
            'date_of_birth',
            'address',
            'image',
            'phone',
        )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.form_name = 'reg_form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'state',
            'local_government',
            'nationality',
            'occupation',
            'gender',
            'date_of_birth',
            'address',
            'image',
            'phone',

            ButtonHolder(
                Submit('register user', 'Register user', css_class='btn-primary')
            )
        )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',


        )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.form_name = 'user_reg_form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

            ButtonHolder(
                Submit('register user', 'Sign up user', css_class='btn-primary')
                )
            )
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #
    #
    #     if commit:
    #         user.save()
    #
    #     return user




class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )














# class RegistrationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             '__all__',
#             ButtonHolder(
#                 Submit('register', 'Register', css_class='btn-primary')
#             )
#         )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn btn-info btn-round btn-lg btn-block')
            )
        )