import csv
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = "load movies from csv inti DB"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', errors='ignore') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                movies = Movie.objects.get_or_create(
                    title = str(row[7]),
                    plot = str(row[8]),
                    director  =str(row[23]),
                    cast = str(row[21])
                )