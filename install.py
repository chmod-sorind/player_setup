#!/usr/bin/python3

import os
import subprocess

pkg = input("what package would you like to install?\n")

print("Installing %s..." % pkg)
subprocess.check_call(['apt-get', '-y', 'install', pkg], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Installation done.")
print("Updating...")
subprocess.check_call(['apt-get', '-y', 'update'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Upgrading..")
subprocess.check_call(['apt-get', '-y', 'upgrade'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Cleaning...")
subprocess.check_call(['apt-get', '-y', 'autoremove'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'autoclean'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Done.")