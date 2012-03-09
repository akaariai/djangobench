import calendar
from datetime import datetime
import os
import simplejson
import subprocess

from settings import *
if __name__ == '__main__':
    os.chdir(GIT_DIR)
    subprocess.check_output(['git', 'checkout', 'master'])
    subprocess.check_output(['git', 'pull', 'upstream', 'master'])
    for test_name, cutpoint_commit, addopts in TESTS:
        # Make sure directories exist
        target_dir = '%s%s/' % (RESULTS_DIR, test_name)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        target_dir_raw = '%sraw/' % target_dir
        if not os.path.exists(target_dir_raw):
            os.mkdir(target_dir_raw)
        output = subprocess.check_output(['git', 'log',  '%s..' % cutpoint_commit])
        lines = output.split('\n')
        for pos, line in enumerate(lines):
            if not line.startswith('commit'):
                continue
            commit = line[7:]
            cmd = ['python', DJANGOBENCH, '--vcs=git',
                    '--control=%s' % commit,  '--control-only', '-r',
                    target_dir_raw]
            for k, v in addopts.items():
                cmd.append(k)
                cmd.append(v)
            cmd.append(test_name)
            if pos == 0:
                for i in range(0, 3):  
                    # Do a little warmup run. On my laptop this is necessary...
                    subprocess.call(cmd)
            if os.path.exists('%s%s.json' % (target_dir_raw, commit)):
                print 'skipping %s: file already exists' % commit
                continue
            subprocess.call(cmd)
        # Now lets turn the raw data into timeseries data suitable for Flot.
        subprocess.check_output(['git', 'checkout', 'master'])
        output = subprocess.check_output(['git', 'log', '--date=iso', '%s..' % cutpoint_commit])
        lines = output.split('\n')
        flot_data = []
        flot_metadata = []
        for pos, line in enumerate(lines):
            if line.startswith('commit'):
                commit = line[7:]
                f = open('%s%s.json' % (target_dir_raw, commit), 'r')
                f.seek(0)
	        data = simplejson.loads(f.read())
                f.close()
                # _very_ crude outlier removal
                data.sort()
                results = data[2:len(data)-2]
                flot_data.append(sum(results)/len(results))
                # (commit id, author and date, actual commit message)
                flot_metadata.append([lines[pos] + '\n' + lines[pos + 1] + '\n' + lines[pos + 2], lines[pos + 4]])
        
        flot_data = [[i, d] for i, d in zip(range(len(flot_data), 0, -1), flot_data)]
        flotdata = open('%sflot.json' % target_dir, 'w+')
        # There might be a better way to pass JSON data than this...
        flotdata.write('var data = ')
        flotdata.write(simplejson.dumps(flot_data))
        flotdata.write(';\nvar metadata = ')
        flotdata.write(simplejson.dumps(flot_metadata))
        flotdata.write(';\nvar version="%s"' % datetime.now())
        flotdata.close()
