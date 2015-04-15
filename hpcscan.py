# hpcscan.py
# Author: Aled Rhys Evans <evansar6@cardiff.ac.uk>
# License: Simplified BSD License (FreeBSD License) 
# Description: An utility to look at Capture-HPC logs and determine if a particular set of logs
#              displays malicious actions by comparing it to profiles of logs already determined
#              to be malicious. This is under active development and is not for production use yet. 
import os, sys, subprocess, getopt, profiles
#from profiles import *

def update():
    subprocess.call('./upgrade.sh', cwd=os.getcwd()+'/extensions/')
    sys.exit(0)

def main(argv):

    try:
        opts, args = getopt.getopt("u", ["update"])
    except getopt.GetoptError:
        print "Error. Exiting."
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--update"):
            update()


    print "Modules loaded:",
    for module in profiles.__all__:
        print module,

    print ""

    for module in profiles.__all__:
        exec '%s = profiles.%s.%s()' % (module, module, module)
        exec 'print %s.greet' % module

main(sys.argv)
update()
