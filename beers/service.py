from django_filters import rest_framework as filters
from beers.models import Beer

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class BeerFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Beer
        fields = ['category']
