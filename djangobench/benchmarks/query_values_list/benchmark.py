from djangobench.utils import run_benchmark
from query_values_list.models import Book

def setup():
    Book.objects.all().delete()
    Book.objects.bulk_create([Book(i, i) for i in range(1000, 1050)])
    Book.objects.bulk_create([Book(i, i) for i in range(1050, 1100)])
    Book.objects.bulk_create([Book(i, i) for i in range(1100, 1150)])
    Book.objects.bulk_create([Book(i, i) for i in range(1150, 1200)])

def benchmark():
    for i in range(0, 10):
        list(Book.objects.values_list('title', 'd1', 'd2', 'd3', 'd4', 'd5'))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.values_list() call.',
    }
)
