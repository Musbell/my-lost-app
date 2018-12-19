from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
# from django.core.urlresolvers import
from django.conf import settings
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    PasswordResetForm
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.tokens.PasswordResetTokenGenerator import token_generator

from django.core.mail import send_mail

from .forms import *

# Create your views here.
class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = '/dashboard'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)





class LogOutView(generic.RedirectView):
    url = '/index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)



def login_redirect(request):
    return redirect('accounts/login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # profile_form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = profile_form.save()
            # and profile_form.is_valid():
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts/profile')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def profile(request):

    args = {'user': request.user}
    return render(request, 'accounts/user_profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


# class PasswordResetView:
#     template_name = 'accounts/password_reset_form.html'
#     form_class = PasswordResetForm
#     # token_generator = default_token_generator
#     success_url = 'login/'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     extra_context = {}



