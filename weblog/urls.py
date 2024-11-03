from django.urls import path
from .views import WeblogView
urlpatterns = [
    path('', WeblogView.as_view() ,name='weblog')
]