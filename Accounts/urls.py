from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,

)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Accounts.views import LoginView, LogOutView
from . import views


app_name = 'accounts'

urlpatterns = [
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogOutView.as_view(), name='logout'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path('profile/edit', views.edit_profile, name='edit_profile'),
        path('change-password/', views.change_password, name='change_password'),
        path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
        path('reset-password/confirm/<uidb64>/<token>/',  PasswordResetConfirmView.as_view(),
             name='password_reset_confirm'),
        path('reset-password/done', PasswordResetDoneView.as_view(), name='reset_password_done'),
        path('reset-password/complete', PasswordResetCompleteView.as_view(), name='reset_password_complete'),
        # path('suggest-list/', views.suggest_view, name='suggest_list'),
        # path('suggest-detail/(?P<pk>\d+)', views.suggest_detail, name='suggest_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
