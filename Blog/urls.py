from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BlogView, BlogDetailView, blog


app_name = 'blog'

urlpatterns = [
        path('blog-post/', BlogView.as_view(), name='blog-post'),
        path('blog/', blog, name='blog_page'),
        path('blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
