import django_filters
from .models import Item, Debtor


class ItemFilter(django_filters.FilterSet):
    itemcode = django_filters.CharFilter(label='Itemcode', lookup_expr="icontains")
    description = django_filters.CharFilter(label='Description', lookup_expr="icontains")
    baseuom = django_filters.CharFilter(label='UOM', lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ['itemcode', 'description', 'baseuom', ]


class CustomerFilter(django_filters.FilterSet):
    # accno = django_filters.CharFilter(label='Account Number', lookup_expr="icontains")
    companyname = django_filters.CharFilter(label='Company Name ', lookup_expr="icontains")

    class Meta:
        model = Debtor
        fields = ['companyname']
