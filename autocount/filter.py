import django_filters
from .models import Item


class ItemFilter(django_filters.FilterSet):
    itemcode = django_filters.CharFilter(label='Itemcode', lookup_expr="icontains")
    description = django_filters.CharFilter(label='Description', lookup_expr="icontains")
    baseuom = django_filters.CharFilter(label='UOM', lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ['itemcode', 'description','baseuom',]
