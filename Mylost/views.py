from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.db.models import Count
from django.contrib import messages
from django.views import generic
from django.shortcuts import render, redirect
from .models import ReportModel, Suggestion, AgentRequest, FoundModel
from .forms import ReportForm, SuggestForm, AgentRequestForm
import operator
from django.db.models import Q

# Create your views here.

class IndexView(SuccessMessageMixin, CreateView):
    template_name = "mylost/index.html"
    model = ReportModel
    form_class = ReportForm
    success_url = '/index'
    success_message = "%(deviceName)s was reported successfully"




def dashboard1(request):
    reports = ReportModel.objects.count()

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


class AgentRequestView(SuccessMessageMixin, CreateView):
    template_name = "mylost/agent_request.html"
    model = AgentRequest
    form_class = AgentRequestForm
    success_url = '/index'
    success_message = "%(name)s message was sent successfully"


def suggest_view(request):
    suggests = Suggestion.objects.all()
    context = {'suggests': suggests}

    return render(request, 'mylost/suggest_list.html', context)




# def suggest_detail(request, pk=None):
#     if pk:
#         suggest = Suggestion.objects.get(pk=pk)
#     else:
#         customer_prof = request.customer_prof
#
#     args = {'suggest': suggest}
#
#     return render(request, 'admin/suggest_detail.html', args)
class SuggestDetailView(generic.DetailView):
    model = Suggestion
    template_name = 'admin/suggest_detail.html'



class AboutView(TemplateView):
    model = Suggestion
    template_name = 'mylost/about.html'


class TermsView(TemplateView):
    model = Suggestion
    template_name = 'mylost/terms.html'



def scan(request):
    print(request.session)
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = ReportModel.objects.filter(Q(serialNumber__iexact=srch))


            if match:
                found = match
                FoundModel = found
                return render(request, 'admin/scan.html', {'sr': match})
            else:
                messages.error(request, 'No result yet for the requested device!')
        else:
            return redirect('/scan/')

    return render(request, 'admin/scan.html')










def foundView(request):
    # reports = ReportModel.objects.all()

    # context = {'reports': reports}
    # request.session.get("found")
    return render(request, 'admin/found.html')
