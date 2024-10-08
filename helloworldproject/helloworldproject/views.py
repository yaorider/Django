'''
Created on 2024/02/13

@author: 8million
'''
from django.http import HttpResponse
from django.views.generic.base import TemplateView

def helloworldfunc(request):
    resopnseobject = HttpResponse('<h1>Hell World</h1>')
    return resopnseobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'