from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Accounts.views import LoginView, LogOutView
from . import views
from django.urls import reverse, reverse_lazy



app_name = 'accounts'

urlpatterns = [
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogOutView.as_view(), name='logout'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path('profile/edit', views.edit_profile, name='edit_profile'),
        path('change-password/', views.change_password, name='change_password'),
        # path('password_change/done/', name='password_change_done'),
        path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html',
            email_template_name="accounts/password_reset_email.html",
            success_url=reverse_lazy('accounts:password-reset-done')
                                                                     ),
             name='reset_password'),
        path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done_form.html'),
             name='reset_password_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'),
             name='password_reset_confirm'),

        # path('reset-password/confirm/<uidb64>/<token>/',  PasswordResetConfirmView.as_view(),
        #      name='password_reset_confirm'),
        # path('reset-password/done', PasswordResetDoneView.as_view(), name='reset_password_done'),
        # path('reset-password/complete', PasswordResetCompleteView.as_view(), name='reset_password_complete'),
        # # path('suggest-list/', views.suggest_view, name='suggest_list'),
        # path('suggest-detail/(?P<pk>\d+)', views.suggest_detail, name='suggest_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
