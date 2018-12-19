from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms
from Blog.models import Blog, Comments, SubscribeMail
import datetime
from datetime import datetime, timedelta
from django.conf import settings

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            # 'updated',
            'author',
            'title',
            'image',
            'content',



        )

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.form_name = 'BlogForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # 'updated',
            'author',
            'title',
            'image',
            'content',



            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-success')
            )
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            'name',
            'image',
            'email',
            'comment',



        )

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.form_name = 'CommentForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'image',
            'email',
            'comment',



            ButtonHolder(
                Submit('Submit', 'Post', css_class='btn-success')
            )
        )




class SubscriberForm(forms.ModelForm):
    class Meta:
        model = SubscribeMail
        fields = (
            'name',
            'email',




        )

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)

        self.form_name = 'SubscriberForm'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',




            ButtonHolder(
                Submit('Submit', 'Sign up', css_class='btn-success')
            )
        )


