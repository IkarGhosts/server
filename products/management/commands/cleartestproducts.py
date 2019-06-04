from django.core.management.base import BaseCommand, CommandError
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **option):
        try:
            query = Product.objects.filter(title__startswith='[test]')
            query.delete()
            self.stdout.write(
                self.style.SUCCESS('Test products succesed removed.')
            )
        except Exception as err:
            raise CommandError(err)
