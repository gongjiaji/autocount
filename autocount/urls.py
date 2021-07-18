from django.urls import path
from .views import *


urlpatterns = [
    path('', TableView.as_view(), name='home'),
    # path('<int:dockey>', CustomerView.as_view(), name='item'),
    path('<int:dockey>', item, name='item'),
    path('<int:dockey>/<str:customer>', customerOrder, name='customerOrder')
]