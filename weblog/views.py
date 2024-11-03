#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views import View

from django.views.generic import TemplateView

#def weblog(request):
#    return render(request, 'home.html')

class WeblogView(TemplateView):
    template_name='home.html'
    #def get(self, request):
    #    return render(request, 'home.html')