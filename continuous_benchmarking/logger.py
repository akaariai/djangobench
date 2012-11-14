import calendar
from datetime import datetime
import os
import simplejson
import subprocess

from settings import *
if __name__ == '__main__':
    curr_dir = os.getcwd()
    os.chdir(GIT_DIR)
    subprocess.Popen(['git', 'checkout', 'master'], stdout=subprocess.PIPE).communicate()
    subprocess.Popen(['git', 'pull', 'upstream', 'master']).communicate()
    for test_name, cutpoint_commit, addopts in TESTS:
        # Make sure directories exist
        target_dir = '%s%s/' % (RESULTS_DIR, test_name)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        target_dir_raw = '%sraw/' % target_dir
        if not os.path.exists(target_dir_raw):
            os.mkdir(target_dir_raw)
        output = subprocess.Popen(['git', 'log', '%s..'%cutpoint_commit, '--', 'django/'], stdout=subprocess.PIPE).communicate()[0]
        lines = list(output.split('\n'))[::-1]
        last_run_time = None
        lines = [l for l in lines if l.startswith('commit')]
        idx = 0
        while idx < len(lines):
            line = lines[idx]
            idx += 1
            commit = line[7:]
            cmd = ['python', DJANGOBENCH, '--vcs=git',
                    '--control=%s' % commit,  '--control-only', '-r',
                    target_dir_raw]
            for k, v in addopts.items():
                cmd.append(k)
                cmd.append(v)
            cmd.append(test_name)
            #if pos == 0:
            #    for i in range(0, 3):  
            #        # Do a little warmup run. On my laptop this is necessary...
            #        subprocess.call(cmd)
            ran_commit = False
            if os.path.exists('%s%s.json' % (target_dir_raw, commit)):
                # print 'skipping %s: file already exists' % commit
                pass
            else:
                print "At commit %s" % commit
                ran_commit = True
                subprocess.call(cmd)
                subprocess.call(["git", "clean", "-fd"])
            try:
                if ran_commit:
	            with open('%s%s.json' % (target_dir_raw, commit), 'r') as f:
	                data = simplejson.loads(f.read())
                    result = sum(data) / len(data)
                    print "got result %s for commit %s" % (result, commit)
                    # Try to remove outliers by comparing to the last result.
                    if last_run_time and abs((last_run_time - result)) > 0.02 * last_run_time:
                        print 'Retrying commit %s - results deviate from last (%s) to (%s)' % (commit, last_run_time, result)
                        os.remove('%s%s.json' % (target_dir_raw, commit))
                        idx -= 1
                    # Note - if the result above was real change in run time, we
                    # rerun the same commit against the changed result and see no
                    # deviation -> success.
                    last_run_time = result
            except Exception, e:
                print 'Problem with commit %s, got exception %s' %(commit, e)
        # Now lets turn the raw data into timeseries data suitable for Flot.
        subprocess.Popen(['git', 'checkout', 'master'], stdout=subprocess.PIPE).communicate()[0]
        output = subprocess.Popen(['git', 'log', '--date=iso', '%s..' % cutpoint_commit,  '--', 'django/'], stdout=subprocess.PIPE).communicate()[0]
        lines = output.split('\n')
        flot_data = []
        flot_metadata = []
        for pos, line in enumerate(lines):
            if line.startswith('commit'):
                commit = line[7:]
                try:
                    f = open('%s%s.json' % (target_dir_raw, commit), 'r')
	            data = simplejson.loads(f.read())
                    f.close()
                except Exception, e:
                    print 'Problem with commit %s, got exception %s' %(commit, e)
                result = sum(data) / len(data)
                flot_data.append(result)
                # (commit id, author and date, actual commit message)
                flot_metadata.append([lines[pos] + '\n' + lines[pos + 1] + '\n' + lines[pos + 2], lines[pos + 4]])
        
        os.chdir(curr_dir)
        flot_data = [[i, d] for i, d in zip(range(len(flot_data), 0, -1), flot_data)]
        flotdata = open('%sflot.js' % target_dir, 'w+')
        # There might be a better way to pass JSON data than this...
        flotdata.write('var data = ')
        flotdata.write(simplejson.dumps(flot_data))
        flotdata.write(';\nvar metadata = ')
        flotdata.write(simplejson.dumps(flot_metadata))
        flotdata.write(';\nvar version="%s"' % datetime.now())
        flotdata.close()
        with open('example.html', 'r') as html_base_file:
            contents = html_base_file.read()
            contents = contents.replace('{{TEST_NAME}}', test_name)
            with open('%sindex.html' % target_dir, 'w') as final_html:
                final_html.write(contents)
        os.chdir(GIT_DIR)
