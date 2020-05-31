from django.core.management.base import BaseCommand, CommandError
from restapi.productapi.views import ProductListView, ProductDetailView
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Custom management commands'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        total = options['total']

        # adding dummy data
        try:
            for i in range(total):
                ProductListView.post(id=get_random_string(),real_time=get_random_string())
                self.stdout.write('New "%id" user post success!' % (id))
        except Exception as e:
            self.stdout.write('Error',e)

        self.stdout.write(ProductListView.get())
