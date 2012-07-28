from djangobench.utils import run_benchmark
from model_init_core_fields.models import Book

def benchmark():
    list(Book.objects.iterator())

def setup():
    for i in range(0, 500):
        Book(pk=i,title='foobar_%s' % i ).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'Fetch objects from DB with ImageField + generic foreign key in other models.',
    }
)
