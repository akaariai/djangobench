from djangobench.utils import run_benchmark
from query_defer.models import MultiField

def benchmark():
    list(MultiField.objects.only('id', 'field1'))

def setup():
    # Make sure there are no objs from previous runs.
    MultiField.objects.all().delete()
    for i in range(0, 1000):
        kwargs = {}
        for j in range(1, 11):
            kwargs['field%s' % j] = 'foobar_%s_%s' % (i, j)
        MultiField(**kwargs).save(force_insert=True)

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects and large number of fields.',
    }
)
