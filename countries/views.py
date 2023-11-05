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
    queryset = Country.objects.filter(common_name__icontains=common_name)
    if not queryset.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CountrySerializer(queryset.first())
    return Response(serializer.data, status=status.HTTP_200_OK)
