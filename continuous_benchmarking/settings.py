GIT_DIR = '/home/akaariai/Programming/djbench/'
DJANGOBENCH = '/home/akaariai/Programming/djangobench/djangobench/main.py'
RESULTS_DIR = '/home/akaariai/tmp/'
# A list of test to run: (djbench test name, first git commit to use for
# running, dict of parameters to pass to djangobench)
TESTS = [
    ('url_resolve', 'a91fb321d8828d71975426466e497f1c6e3c9b71', {'-t': '30'}),
    #('query_all', 'a91fb321d8828d71975426466e497f1c6e3c9b71', {'-t': '20'})
]
