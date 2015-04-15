# hpcscan.py
# Author: Aled Rhys Evans <evansar6@cardiff.ac.uk>
# License: Simplified BSD License (FreeBSD License) 
# Description: An utility to look at Capture-HPC logs and determine if a particular set of logs
#              displays malicious actions by comparing it to profiles of logs already determined
#              to be malicious. 
import os, sys, profiles
from profiles import *

print "Modules loaded:",
for word in profiles.__all__:
    print word,

print ""

vir = flashcache.flashcache()
print vir.greet
