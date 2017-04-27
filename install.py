#!/usr/bin/python3

import os
import subprocess

subprocess.check_call(['apt-get', '-y', 'install', 'htop'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'update'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'upgrade'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'autoremove'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'autoclean'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
