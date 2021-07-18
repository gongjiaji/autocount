from django.shortcuts import render
from .models import Item, ItemTable, Itemuom, Debtor, CustomerTable
from django.views.generic import ListView
import django_tables2 as tables
from django_filters.views import FilterView
from .filter import ItemFilter


# Create your views here.
# def home(request):
#     items = Item.objects.all()
#     itemFilter = ItemFilter(request.GET, queryset=items)
#     items = itemFilter.qs
#
#     return render(request, "autocount/dashboard.html", locals())
class TableView(tables.SingleTableMixin,FilterView):
    model = Item
    table_class = ItemTable
    queryset = Item.objects.all()
    template_name = "autocount/dashboard2.html"
    filterset_class = ItemFilter
