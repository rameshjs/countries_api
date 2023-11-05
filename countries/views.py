from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from countries.models import Country
from countries.serializers import CountrySerializer
from countries.filters import CountriesFilters


@api_view(["GET"])
def country_list(request):
    queryset = Country.objects.all()
    filterset = CountriesFilters(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs
    serializer = CountrySerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def country(request, common_name):
    queryset = Country.objects.get(common_name=common_name)
    serializer = CountrySerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)
