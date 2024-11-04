#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views import View
from .models import Weblog
from django.views.generic import TemplateView
from django.views.generic import ListView
#def weblog(request):
#    return render(request, 'home.html')

class WeblogView(TemplateView):
    template_name='home.html'
    #def get(self, request):
    #    return render(request, 'home.html')
class WeblogView(ListView):
    model =Weblog
    template_name='home.html'