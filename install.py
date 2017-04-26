import os, subprocess

subprocess.check_call(['apt-get', 'install', 'htoo'], stdout=open(os.devnull,'wb'), stderr=subprocess.STDERR)

