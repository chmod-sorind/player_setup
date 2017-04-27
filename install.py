#!/usr/bin/python3

import os
import subprocess
import argparse
import sys


# Override the default behavior of the error method
class BSParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = BSParser(description='Install packages')
parser.add_argument('-p', '--pkg', action='store', nargs='?', help='Some help for this argument')
args = parser.parse_args()

print("Installing %s..." % args.pkg)
subprocess.check_call(['apt-get', '-y', 'install', args.pkg], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Installation done.")
print("Updating...")
subprocess.check_call(['apt-get', '-y', 'update'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Upgrading..")
subprocess.check_call(['apt-get', '-y', 'upgrade'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Cleaning...")
subprocess.check_call(['apt-get', '-y', 'autoremove'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
subprocess.check_call(['apt-get', '-y', 'autoclean'], stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
print("Done.")