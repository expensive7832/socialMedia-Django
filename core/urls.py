from django.urls import path
from .views import Home, index

urlpatterns = [
    path('', Home, name='home'),
    
]