from django.core.management.base import BaseCommand
import json

# Models
from countries.models import Currency


class Command(BaseCommand):
    help = "Load currency data from JSON and add it to the database"

    def handle(self, *args, **options):
        json_file_path = "countriesV1.json"

        try:
            with open(json_file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("JSON file not found."))
            return

        for item in data:
            for currency in item["currencies"]:
                existing_currency = Currency.objects.filter(code=currency)
                if existing_currency.exists():
                    existing_currency.update(
                        name=item["currencies"][currency]["name"],
                        symbol=item["currencies"][currency]["symbol"],
                    )
                else:
                    Currency.objects.create(
                        code=currency,
                        name=item["currencies"][currency]["name"],
                        symbol=item["currencies"][currency]["symbol"],
                    )

        self.stdout.write(
            self.style.SUCCESS("Currency data loaded and added to the database.")
        )
