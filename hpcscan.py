# hpcscan.py
# Author: Aled Rhys Evans <evansar6@cardiff.ac.uk>
# License: Simplified BSD License (FreeBSD License) 
# Description: An utility to look at Capture-HPC logs and determine if a particular set of logs
#              displays malicious actions by comparing it to profiles of logs already determined
#              to be malicious. This is under active development and is not for production use yet. 
import os, sys, subprocess, getopt, profiles
#from profiles import *

def usage():
    print "Help for hpcscan.py:"
    print "Usage: python hpcscan.py <option> <argument>"
    print "Options include:"
    print "\t-u (--update):\t\t\t\t updates the application from github repo"
    print "\t-f <filename> (--file <filename>):\t specifies the file to be analysed"
    

def update():
    subprocess.call('./upgrade.sh', cwd=os.getcwd()+'/extensions/')
    sys.exit(0)

def main():

    if len(sys.argv) < 2:
        usage()
        exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'uf:h', ['update', 'file=', 'help'])
    except getopt.GetoptError:
        print "Unrecognised option. Showing usage information:"
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-u', '--update'):
            update()
        elif opt in ('-f', '--file'):
            print "Checking for file %s..." % arg,
            if not os.path.exists(arg):
                print "\bI/O Error: File does not exist."
                exit(1)
            else:
                print "\bokay."
                log = open(arg, "rb") 
        elif opt in ('-h', '--help'):
            usage()
            exit(0)
        else:
            print "Unparsed argument."
            exit(1)

    print "Checking loaded modules..."
    for module in profiles.__all__:
        print module,
    print ""

    for module in profiles.__all__:
        exec '%s = profiles.%s.%s()' % (module, module, module)
        exec 'print %s.greet' % module

    log.close()

main()
