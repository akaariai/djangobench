GIT_DIR = '/home/akaariai/Programming/djbench/'
DJANGOBENCH = '/home/akaariai/Programming/djangobench/djangobench/main.py'
RESULTS_DIR = '/home/akaariai/tmp/'
# A list of test to run:
#   - djangobench test name
#   - earliest git commit to include in the benchmark
#   - dict of parameters to pass to djangobench)
TESTS = [
    #('url_resolve', 'f7a7b09c051faa751b5138d8fc517dbb841caa45', {'-t': '30'}),
    #('query_all', 'f7a7b09c051faa751b5138d8fc517dbb841caa45', {'-t': '20'}),
    #('query_all_multifield', 'f7a7b09c051faa751b5138d8fc517dbb841caa45', {'-t': '20'}),
    #('url_reverse', 'f7a7b09c051faa751b5138d8fc517dbb841caa45', {'-t': '30'}),
    ('query_annotate', '82a76ef67d944b1a4507cac81476bebba0c90e4a', {'-t': '30'}),
]
