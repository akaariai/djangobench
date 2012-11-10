from djangobench.utils import run_benchmark
from query_values_list.models import Book

def setup():
    Book.objects.all().delete()
    for i in range(1000, 1200):
        Book.objects.create(i, i)

def benchmark():
    list(Book.objects.values_list('title', 'd1', 'd2', 'd3', 'd4', 'd5'))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.values_list() call.',
    }
)
