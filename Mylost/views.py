from django.conf import settings
# from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.template.loader import get_template

from .forms import ReportForm, SuggestForm, AgentRequestForm
from .models import ReportModel, Suggestion, AgentRequest, FoundModel
# from collections import OrderedDictb


# Create your views here.
def checker_view(request):
    if request.method == 'POST':
        srch2 = request.POST['srh1']

        if srch2:
            match1 = ReportModel.objects.filter(Q(serialNumber__iexact=srch2))


            if match1:

                return render(request, 'mylost/checker.html', {'sr1': match1})
            else:
                messages.error(request, 'No result yet for the requested device!')
        else:
            return redirect('/index/')

    return render(request, 'mylost/checker.html')



class IndexView(SuccessMessageMixin, CreateView):
    template_name = "mylost/index.html"
    model = ReportModel
    form_class = ReportForm
    success_url = '/index'
    success_message = "%(deviceName)s was reported successfully"






def dashboard1(request):
    reports = ReportModel.objects.count()
    suggest = Suggestion.objects.count()
    requests = AgentRequest.objects.count()
    # found   =  ReportModel.device_status.count()

    context = {'reports': reports,
               'suggest': suggest,
               'requests': requests}

    return render(request, 'admin/admin_index.html', context)



def reports_view(request):
    reports = ReportModel.objects.all()
    context = {'reports': reports}

    return render(request, 'admin/reports.html', context)

class SuggestSendView(SuccessMessageMixin, CreateView):
    template_name = "mylost/suggest.html"
    model = Suggestion
    form_class = SuggestForm
    success_url = '/suggest'
    success_message = "%(name)s message was sent successfully"


class AgentRequestView(SuccessMessageMixin, CreateView):
    template_name = "mylost/agent_request.html"
    model = AgentRequest
    form_class = AgentRequestForm
    success_url = '/agent-request'
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
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = ReportModel.objects.filter(Q(serialNumber__iexact=srch))


            if match:
                match.update(device_status='FOUND')
                subject = 'Congratulations!your device is been found.'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [settings.DEFAULT_FROM_EMAIL]
                #
                # context = {
                #     'match': match
                #
                # }

                # found_message = get_template('mylost/found_message.txt').render(context)
                found_message = f'Congratulations! Your device' \
                                # f'with the IMEI number {match.serialNumber}has been found! kindly visit one of our ' \
                                # f' centers ot the nearest police station to claim and retrieve your device'
                send_mail(subject=subject, message=found_message, from_email=from_email, recipient_list=to_email,
                          fail_silently=True)


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
