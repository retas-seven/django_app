# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:07:20 2018

@author: osawa
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]