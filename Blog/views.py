from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Blog, SubscribeMail, Comments
from .forms import BlogForm, SubscriberForm, CommentForm

# Create your views here.

class BlogView(SuccessMessageMixin, CreateView):
    template_name = "admin/blog_post.html"
    model = Blog
    form_class = BlogForm
    success_url = '/blog-post'
    success_message = "%(title)s was created successfully"



def blog(request):

    top_post = Blog.objects.all()[::-1]
    recent_post = Blog.objects.all()[::-1]

    context = {'top_posts': top_post, 'recent_posts': recent_post}

    return render(request, 'blog/home.html', context)




class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    # def get_queryset(self):
    #     related_post = Blog.objects.all()[::-1]
    #     """Return the last five published posts."""
    #     return related_post



class CommentView(SuccessMessageMixin, CreateView):
    model = Comments
    form_class = CommentForm
    success_url = '/blog-detail'
    template_name = 'blog/comment'


class SubscribeView(SuccessMessageMixin, CreateView):
    template_name = "blog/subscribe.html"
    model = SubscribeMail
    form_class = SubscriberForm
    success_url = '/blog'
    success_message = "You have successfully subscribe to our newsletter"