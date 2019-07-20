"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})

urlpatterns = [
    # django all-auth関連
    path('accounts/', include('allauth.urls')),
    # 独自機能
    path('', TemplateView.as_view(template_name='top.html'), name='top'),
    path('home/', HomeView.as_view(), name='home'),
    path('shohin/', include('shohin.urls')),
    path('nohin/', include('nohin.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
