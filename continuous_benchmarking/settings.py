GIT_DIR = '/home/akaariai/Programming/djbench/'
DJANGOBENCH = '/home/akaariai/Programming/djangobench/djangobench/main.py'
RESULTS_DIR = '/home/akaariai/tmp/'
# A list of test to run: (djbench test name, first git commit to use for
# running, dict of parameters to pass to djangobench)
TESTS = [
    ('url_resolve', 'c2c622dc045c025e44417a32371991b436118861', {'-t': '30'}),
    ('query_all', 'c2c622dc045c025e44417a32371991b436118861', {'-t': '20'})
]
