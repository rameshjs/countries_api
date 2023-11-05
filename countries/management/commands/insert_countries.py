from django.core.management.base import BaseCommand
import json

# Models
from countries.models import Country, Currency


class Command(BaseCommand):
    help = "Load country data from JSON and add it to the database"

    def handle(self, *args, **options):
        json_file_path = "countriesV1.json"

        try:
            with open(json_file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("JSON file not found."))
            return

        for item in data:
            country_dict = {
                "common_name": item.get("name", {}).get("common", ""),
                "official_name": item.get("name", {}).get("official", ""),
                "native_name": item.get("name", {}).get("nativeName", {}),
                "tld": item.get("tld", ""),
                "cca2": item.get("cca2", ""),
                "ccn3": item.get("ccn3", ""),
                "cca3": item.get("cca3", ""),
                "cioc": item.get("cioc", ""),
                "fifa": item.get("fifa", ""),
                "independent": item.get("independent", False),
                "status": item.get("status", ""),
                "un_member": item.get("unMember", False),
                "idd": item.get("idd", {}),
                "capital": item.get("capital", ""),
                "capital_info": item.get("capitalInfo", {}),
                "alt_spellings": item.get("altSpellings", ""),
                "region": item.get("region", ""),
                "subregion": item.get("subregion", ""),
                "continents": item.get("continents", {}),
                "languages": item.get("languages", {}),
                "translations": item.get("translations", {}),
                "latlng": item.get("latlng", {}),
                "landlocked": item.get("landlocked", False),
                "borders": item.get("borders", {}),
                "area": item.get("area", 0),
                "flag": item.get("flag", ""),
                "demonyms": item.get("demonyms", {}),
                "flags": item.get("flags", {}),
                "coat_of_arms": item.get("coatOfArms", {}),
                "population": item.get("population", 0),
                "maps": item.get("maps", {}),
                "gini": item.get("gini", {}),
                "car": item.get("car", {}),
                "postal_code": item.get("postalCode", {}),
                "start_of_week": item.get("startOfWeek", ""),
                "timezones": item.get("timezones", {}),
            }
            print(country_dict["common_name"])
            currency_info = item.get("currencies", {})

            if not Country.objects.filter(common_name=item["name"]["common"]).exists():
                country = Country.objects.create(**country_dict)

                if currency_info:
                    currency_codes = list(currency_info.keys())
                    related_currencies = Currency.objects.filter(
                        code__in=currency_codes
                    )
                    if related_currencies.exists():
                        country.currencies.add(*related_currencies)
                        country.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Total {Country.objects.count()} countries data loaded and added to the database."
            )
        )
