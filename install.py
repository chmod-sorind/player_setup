#!/usr/bin/python3

import os
import subprocess

subprocess.check_call(['apt-get', 'install', 'htop'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', 'update'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', 'upgrade'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', 'autoremove'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', 'autoclean'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
