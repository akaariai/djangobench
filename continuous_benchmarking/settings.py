GIT_DIR = '/home/akaj/Programming/django/'
DJANGOBENCH = '/home/akaj/Programming/djangobench/djangobench/main.py'
RESULTS_DIR = '/home/akaj/tmp/'
# A list of test to run:
#   - djangobench test name
#   - earliest git commit to include in the benchmark
#   - dict of parameters to pass to djangobench)
MERGE_BASE_DJANGO13 = '7c08f4c6351f7e53a01ff800d8a61f19ca961b29'
TMP_COMMIT = '00ec03fd'
TESTS = [
    ('query_annotate', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('url_resolve', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('url_resolve_flat', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('url_resolve_nested', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('url_reverse', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('query_complex_filter', MERGE_BASE_DJANGO13, {'-t': '20'}),
    ('qs_filter_chaining', MERGE_BASE_DJANGO13, {'-t': '20'}),
    ('query_raw', MERGE_BASE_DJANGO13, {'-t': '20'}),
    ('query_all', MERGE_BASE_DJANGO13, {'-t': '20'}),
    ('query_all_multifield', MERGE_BASE_DJANGO13, {'-t': '20'}),
    ('model_save', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('query_select_related', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('query_delete', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('template_compilation', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('template_render', MERGE_BASE_DJANGO13, {'-t': '30'}),
    ('template_render_simple', MERGE_BASE_DJANGO13, {'-t': '30'}),
]
