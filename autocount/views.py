from django.shortcuts import render, redirect
from .models import Item, ItemTable, Itemuom, Debtor, CustomerTable
from django.views.generic import ListView
import django_tables2 as tables
from django_filters.views import FilterView
from .filter import ItemFilter, CustomerFilter
from .forms import OrderForm


class TableView(tables.SingleTableMixin, FilterView):
    model = Item
    table_class = ItemTable
    queryset = Item.objects.all()
    template_name = "autocount/dashboard2.html"
    filterset_class = ItemFilter


def roundValue(val, digits=2):
    if val is not None or val == 0E-8:
        val = round(val, digits)
    else:
        val = "No value"
    return val


def itemView(request, dockey):
    queryset = Debtor.objects.all()
    filter = CustomerFilter(request.GET, queryset=queryset)
    customers = filter.qs
    item = Item.objects.get(dockey=dockey)
    itemuom = Itemuom.objects.get(itemcode=item.itemcode, uom=item.baseuom)

    cost = roundValue(itemuom.cost)
    price = roundValue(itemuom.price)
    price2 = roundValue(itemuom.price2)
    minsaleprice = roundValue(itemuom.minsaleprice)
    balqty = roundValue(itemuom.balqty, 0)

    return render(request, "autoCount/item.html", locals())


# itemCode/customer  卖某个产品给某个客户
def customerOrder(request, dockey, accno):
    # 获取要卖的 item
    item = Item.objects.get(dockey=dockey)
    itemuom = Itemuom.objects.get(itemcode=item.itemcode, uom=item.baseuom)
    cost = roundValue(itemuom.cost)
    price = roundValue(itemuom.price)
    price2 = roundValue(itemuom.price2)
    minsaleprice = roundValue(itemuom.minsaleprice)
    balqty = roundValue(itemuom.balqty, 0)

    # 获取所有的 Customers
    customer = Debtor.objects.get(accno=accno)

    form = OrderForm()
    return render(request, "autoCount/customerorder.html", locals())


def order(request, dockey, accno):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            price = form['price'].value()
            quantity = form['quantity'].value()
            print(price, quantity)
            print(dockey, accno)
            # TODO: add price quantity dockey accno to create DO
    return redirect("home")
