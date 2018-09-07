from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Mylost.views import IndexView, dashboard1, suggest_view, SuggestSendView, suggest_detail, AboutView, TermsView
from . import views


app_name = 'mylost'

urlpatterns = [
        path('index/', IndexView.as_view(), name='index'),
        path('dashboard/', views.dashboard1, name='dashboard'),
        path('reports/', views.reports_view, name='reports'),
        path('suggest/', SuggestSendView.as_view(), name='suggest'),
        path('suggest-list/', views.suggest_view, name='suggest_list'),
        path('suggest-detail/(?P<pk>\d+)', views.suggest_detail, name='suggest_detail'),
        path('about/', AboutView.as_view(), name='about'),
        path('terms/', TermsView.as_view(), name='terms'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
