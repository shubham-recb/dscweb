"""dscweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_view, about_view, register_view
from blog.views import blog_post_create_view
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('register/', register_view, name='register'),
    path('blog-new/', blog_post_create_view, name='new_blog'),
    path('blog/', include('blog.urls', namespace='blog')), 
    path('courses/', include('courses.urls', namespace='courses')),

]


if settings.DEBUG:
    #test mode
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

