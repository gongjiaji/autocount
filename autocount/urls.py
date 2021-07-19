from django.urls import path
from .views import *


urlpatterns = [
    path('', TableView.as_view(), name='home'),
    path('<int:dockey>', itemView, name='item'),
    path('<int:dockey>/<str:accno>', customerOrder, name='customerOrder'),
    path('<int:dockey>/<str:accno>/order', order, name='order'),
]