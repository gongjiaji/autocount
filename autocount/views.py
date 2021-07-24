import datetime
import uuid

import django.db.transaction
from django.shortcuts import render, redirect
from .models import Item, ItemTable, Itemuom, Debtor, CustomerTable, Do, Branch, Glmast, Terms, Currency, Users, \
    Location, Dodtl, Itembatch, Taxtype
from django.views.generic import ListView
import django_tables2 as tables
from django_filters.views import FilterView
from .filter import ItemFilter, CustomerFilter
from .forms import OrderForm
from .makeInvoice import exportDo
from .printer import printDo


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
            price = float(form['price'].value())
            quantity = float(form['quantity'].value())
            print(price, quantity, dockey, accno)
            item = Item.objects.get(dockey=dockey)
            itemuom = Itemuom.objects.get(itemcode=item.itemcode, uom=item.baseuom)
            # get last docNo of DO
            lastDo = Do.objects.all().order_by('-docno').first()
            lastDocNo = lastDo.docno
            newDocNo = int(lastDocNo) + 1
            lastDo = Do.objects.all().order_by('-dockey').first()
            lastDocKey = lastDo.dockey
            newDocKey = lastDocKey + 1
            if int(newDocNo) < 8000000:
                newDocNo += 8000000
                newDocNo = str(newDocNo)
            if int(newDocKey) < 8000000:
                newDocKey += 8000000

            # newDocNo = str(lastDocNo).zfill(7)
            debtor = Debtor.objects.get(accno=accno)
            do = Do()
            do.dockey = newDocKey
            do.docno = newDocNo
            do.debtorname = debtor.companyname
            do.docdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            do.description = "DELIVERY ORDER"
            do.total = do.analysisnettotal = do.localanalysisnettotal = do.totalextax = do.taxableamt = do.localtaxableamt = do.taxcurrencytaxableamt = round(
                quantity * price, 2)
            do.footer1amt = do.footer2amt = do.footer3amt = 0
            do.currencyrate = 1
            do.nettotal = do.localnettotal = round(do.total * 1.07, 2)
            do.localtotalcost = itemuom.cost
            do.tax = do.localtax = do.extax = do.localextax = do.taxcurrencytax = do.nettotal - do.total
            do.posttostock = do.transferable = "T"
            do.printcount = 0
            do.cancelled = "F"
            do.lastmodified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # ADD THIS TO THE DB
            do.lastmodifieduserid = do.createduserid = Users.objects.get(userid="JIAJI")
            do.createdtimestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            do.cansync = "F"
            do.lastupdate = 0
            do.saleslocation = Location.objects.get(location="HQ")
            do.guid = uuid.uuid4()
            do.totaxcurrencyrate = 1
            do.calcdiscountonunitprice = "F"
            do.inclusivetax = "F"
            do.roundingmethod = 4
            branch = Branch()
            glmast = Glmast(accno=accno)
            term = Terms(displayterm="C.O.D.")
            currency = Currency(currencycode="SGD")
            branch.accno = glmast
            branch.branchcode = "branch"
            do.debtorcode = branch
            do.displayterm = term
            do.currencycode = currency

            # Make details of this DO
            dodtl = Dodtl()
            # itembatch = Itembatch(itemcode=item.itemcode)
            taxType = Taxtype(taxtype="SR")
            dodtl.dtlkey = dodtl.dockey = do.dockey
            dodtl.seq = 16
            dodtl.mainitem = "T"
            dodtl.uom = itemuom.uom
            dodtl.itemcode = itemuom
            dodtl.location = do.saleslocation
            dodtl.description = item.description
            dodtl.useruom = item.baseuom
            dodtl.qty = quantity
            dodtl.rate = 1
            dodtl.smallestqty = quantity
            dodtl.transferedqty = 0
            dodtl.focqty = 0
            dodtl.smallestunitprice = dodtl.unitprice = price
            dodtl.discountamt = 0
            dodtl.taxtype = taxType
            dodtl.tax = dodtl.localtax = dodtl.taxcurrencytax = do.tax
            dodtl.subtotal = dodtl.localsubtotal = dodtl.taxableamt = dodtl.localsubtotalextax = dodtl.subtotalextax = dodtl.localtaxableamt = dodtl.taxcurrencytaxableamt = do.total
            dodtl.localtotalcost = do.localtotalcost
            dodtl.transferable = "T"
            dodtl.printout = "T"
            dodtl.dtltype = "N"
            dodtl.addtosubtotal = "T"
            dodtl.guid = uuid.uuid4()
            dodtl.deliverydate = do.createdtimestamp
            dodtl.taxrate = 7
            # to be clarified about the acc no
            dodtl.accno = glmast

            with django.db.transaction.atomic():
                do.save()
                dodtl.save()

            # generate do pdf
            exportDo(debtor=do.debtorname, no=do.dockey, tel=debtor.phone1, fax=debtor.fax1, yourpono="", term="C.O.D.",
                     date=datetime.datetime.now().strftime("%Y-%m-%d"), item=item.itemcode,
                     description=item.description, qty=quantity, uom=item.baseuom, total=quantity)
            printDo(fr"C:\Users\rectitude pc-2021-1\Desktop\rectitude\autocount\static\pdf\{do.dockey}.pdf")

    return redirect("home")
