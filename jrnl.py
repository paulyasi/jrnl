#!/usr/bin/env python

# requires .jrnl.conf in your home directory with config format like:
# [jrnl]
# folder = /Users/pyasi/Dropbox/jrnl
# editor = /usr/bin/vim

import os
import sys
import ConfigParser 
import time
import subprocess

from os.path import expanduser
home = expanduser("~")

conf = ConfigParser.ConfigParser()
conf.read(home+"/.jrnl.conf")

folder = conf.get('jrnl','folder')
editor = conf.get('jrnl','editor')

print folder
print editor

new_jrnl_file = folder+"/"+time.strftime("%Y-%m-%d_%H%M")

print new_jrnl_file

subprocess.call([editor, new_jrnl_file])



