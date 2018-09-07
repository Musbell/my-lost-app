from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Blog.views import BlogView, blog_detail
from . import views


app_name = 'blog'

urlpatterns = [
        path('blog-post/', BlogView.as_view(), name='blog-post'),
        path('blog/', views.blog, name='blog_page'),
        path('blog-detail/(?P<pk>\d+)', views.blog_detail, name='blog_detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
