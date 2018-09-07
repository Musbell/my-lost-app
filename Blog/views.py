from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Blog
from .forms import BlogForm

# Create your views here.

class BlogView(SuccessMessageMixin, CreateView):
    template_name = "admin/blog_post.html"
    model = Blog
    form_class = BlogForm
    success_url = '/blog-post'
    success_message = "%(title)s was created successfully"



def blog(request):
    top_post = Blog.objects.all()[::-1]


    context = {'top_posts': top_post}

    return render(request, 'blog/home.html', context)





# class BlogDetailView(generic.DetailView):
#     model = Blog
#     template_name = 'blog/blog_detail.html'



def blog_detail(request, pk=None):
    if pk:
        post = Blog.objects.get(pk=pk)
    else:
        customer_prof = request.customer_prof

    args = {'post': post}

    return render(request, 'blog/blog_detail.html', args)