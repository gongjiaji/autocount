from django.urls import path
from .views import *

urlpatterns = [
    path('', TableView.as_view(), name='home'),
]