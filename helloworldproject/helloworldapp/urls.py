'''
Created on 2024/02/15

@author: 8million
'''
from django.urls import path
from .views import helloworldfunc

urlpatterns = [
        path('helloworldapp/', helloworldfunc)
    ]