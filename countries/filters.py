from django_filters import rest_framework as filters
from countries.models import Country


class CountriesFilters(filters.FilterSet):
    class Meta:
        model = Country
        fields = {
            "common_name": ["icontains"],
            "official_name": ["icontains"],
            "cca2": ["iexact"],
            "ccn3": ["iexact"],
            "cca3": ["iexact"],
            "cioc": ["iexact"],
        }
