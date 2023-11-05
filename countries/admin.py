from django.contrib import admin
from countries.models import Country, Currency


class CountryAdmin(admin.ModelAdmin):
    list_display = ("common_name",)
    search_fields = ("common_name",)


admin.site.register(Country, CountryAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code",)
    search_fields = ("code",)


admin.site.register(Currency, CurrencyAdmin)
