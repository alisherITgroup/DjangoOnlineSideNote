from django.urls import path
from .views import index, add, about

urlpatterns = [
    path('', index,name='home'),
    path('add/', add, name='add'),
    path('about/', about, name='about')
]