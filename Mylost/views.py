from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views import generic
from django.shortcuts import render
from .models import ReportModel, Suggestion
from .forms import ReportForm, SuggestForm

# Create your views here.

class IndexView(SuccessMessageMixin, CreateView):
    template_name = "mylost/index.html"
    model = ReportModel
    form_class = ReportForm
    success_url = '/index'
    success_message = "%(deviceName)s was reported successfully"




def dashboard1(request):
    reports = ReportModel.objects.all()

    context = {'reports': reports}

    return render(request, 'admin/admin_index.html', context)



def reports_view(request):
    reports = ReportModel.objects.all()
    context = {'reports': reports}

    return render(request, 'admin/reports.html', context)

class SuggestSendView(SuccessMessageMixin, CreateView):
    template_name = "mylost/suggest.html"
    model = Suggestion
    form_class = SuggestForm
    success_url = '/index'
    success_message = "%(name)s message was sent successfully"


def suggest_view(request):
    suggests = Suggestion.objects.all()
    context = {'suggests': suggests}

    return render(request, 'mylost/suggest_list.html', context)




def suggest_detail(request, pk=None):
    if pk:
        suggest = Suggestion.objects.get(pk=pk)
    else:
        customer_prof = request.customer_prof

    args = {'suggest': suggest}

    return render(request, 'admin/suggest_detail.html', args)



class AboutView(TemplateView):
    model = Suggestion
    template_name = 'mylost/about.html'


class TermsView(TemplateView):
    model = Suggestion
    template_name = 'mylost/terms.html'




