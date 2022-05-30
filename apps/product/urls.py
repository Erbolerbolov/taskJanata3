from django.urls import path 
from .views import ListCreateProductView


urlpatterns = [ 
    path('list_or_create/', ListCreateProductView.as_view()),
]