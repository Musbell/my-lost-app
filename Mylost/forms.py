from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms
from Mylost.models import ReportModel, Suggestion, AgentRequest
import datetime
from datetime import datetime, timedelta
from django.conf import settings

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = (
            # 'date',
            'deviceName',
            'deviceModel',
            'serialNumber',
            'status',
            'state',
            'email',
            'phone',


        )

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        self.form_name = 'ReportForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # 'date',
            'deviceName',
            'deviceModel',
            'serialNumber',
            'status',
            'state',
            'email',
            'phone',


            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-success')
            )
        )


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = (
            'name',
            'title',
            'email',
            'message',


        )

    def __init__(self, *args, **kwargs):
        super(SuggestForm, self).__init__(*args, **kwargs)

        self.form_name = 'SuggestForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'title',
            'email',
            'message',


            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-success')
            )
        )


class AgentRequestForm(forms.ModelForm):
    class Meta:
        model = AgentRequest
        fields = (
            'name',
            'state',
            'email',
            'address',
            'phone',
            'short_bio',


        )

    def __init__(self, *args, **kwargs):
        super(AgentRequestForm, self).__init__(*args, **kwargs)

        self.form_name = 'AgentRequestForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'state',
            'email',
            'address',
            'phone',
            'short_bio',


            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-success')
            )
        )