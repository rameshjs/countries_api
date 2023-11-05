from rest_framework import serializers
from countries.models import Country, Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = "__all__"
