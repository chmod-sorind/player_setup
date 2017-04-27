#!/usr/bin/python3

import os
import subprocess

subprocess.check_call(['apt-get', 'install', 'htoo'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
