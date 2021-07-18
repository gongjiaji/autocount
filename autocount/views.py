from django.shortcuts import render
from .models import Item, ItemTable, Itemuom, Debtor, CustomerTable
from django.views.generic import ListView
import django_tables2 as tables
from django_filters.views import FilterView
from .filter import ItemFilter


class TableView(tables.SingleTableMixin, FilterView):
    model = Item
    table_class = ItemTable
    queryset = Item.objects.all()
    template_name = "autocount/dashboard2.html"
    filterset_class = ItemFilter

# class CustomerView(tables.SingleTableMixin, FilterView):
#     model = Debtor
#     table_class = CustomerTable
#     queryset = Debtor.objects.all()
#     template_name = "autocount/item.html"
#     filterset_class = ItemFilter

def item(request, dockey):
    # 获取 itemCode 对应的产品信息
    item = Item.objects.get(dockey=dockey)
    # 获取 itemCode 对应的价格信息
    itemuom = Itemuom.objects.get(itemcode=item.itemcode, uom=item.baseuom)
    return render(request, "autoCount/item.html", locals())


# itemCode/customer  卖某个产品给某个客户
def customerOrder(request, dockey, customer):
    # 获取要卖的 item
    item = Item.objects.get(dockey=dockey)
    # 获取所有的 Customers
    return render(request, "autoCount/customerorder.html", locals())
