from djangobench.utils import run_benchmark
from model_init_self_signals.models import Book

def benchmark():
    list(Book.objects.all())

def setup():
    # Make sure there are no books from previous runs.
    Book.objects.all().delete()
    for i in range(0, 1000):
        Book(pk=i,title='foobar_%s' % i ).save(force_insert=True)

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects.',
    }
)
