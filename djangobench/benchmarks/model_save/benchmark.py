import time
from djangobench.utils import run_benchmark
from model_save.models import Book

def benchmark():
    b = Book.objects.get(pk=1)
    b.title = 'bye!' if b.title == 'hi!' else 'hi!'
    b.save()

def setup():
    Book.objects.all().delete()
    Book.objects.create(pk=1, title='hi!')

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'Time of Model.objects.get() + save()',
    }
)
