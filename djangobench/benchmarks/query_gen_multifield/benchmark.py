from djangobench.utils import run_benchmark
from query_gen_multifield.models import MultiField

def benchmark():
    for i in range(0, 10):
        list(MultiField.objects.filter(
            field1=1, field2=2, field3=3, field4=4, field5=5,
            field6=6, field7=7, field8=8, field9=9, field10=10))


def setup():
    # Make sure there are no objs from previous runs.
    MultiField.objects.all().delete()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'Test speed of generating & executing a query for multifield model',
    }
)
