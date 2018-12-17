# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:07:20 2018

@author: osawa
"""

from django.urls import path
from .views import HelloView

urlpatterns = [
    path(r'', HelloView.as_view(), name='index'),
]