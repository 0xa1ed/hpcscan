# hpcscan.py
# Author: Aled Rhys Evans <evansar6@cardiff.ac.uk>
# License: Simplified BSD License (FreeBSD License) 
# Description: An utility to look at Capture-HPC logs and determine if a particular set of logs
#              displays malicious actions by comparing it to profiles of logs already determined
#              to be malicious. This is under active development and is not for production use yet. 
import os
import sys
import subprocess
import getopt
import profiles
import csv
import time


def endwrite():
    outfile = open(outname, "r")
    lines = outfile.readlines()
    outfile.close()
   
    outfile = open(outname, "w")
    outfile.write("HPCScan Log for " + str(time.strftime("%d/%m/%Y")) + ":\n\n") 
    for key, val in scores.iteritems():
        outfile.write(str(key) + " occurrences: " + str(val) + "\n")
    outfile.write("\n" + "Details for suspected malicious matches:" + "\n")

    for line in lines:
        outfile.write(line)

    outfile.close()
    print "Saved log in: %s" % (outname)

def interwrite(prof):
    if 'flashcache' in str(prof):
        pass
    else:
        timestamp = str(time.strftime("%d%m%Y"))
        global outname
        outname = 'out' + timestamp + '.txt' 
        if not os.path.exists(outname):
            outfile = open(outname, "w")
            for key, val in scores.iteritems():
                if key in str(prof):
                    outfile.write("=====================================================\n")
                    outfile.write(key + " instance:\n")
                    outfile.write("=====================================================\n\n")
                    for line in prof.outbuff:
                        if line == "0":
                            pass
                        else:
                            outfile.write(line + "\n")
                    outfile.write("\n\n")
                    outfile.close()
        else:
            outfile = open(outname, "a+")
            for key, val in scores.iteritems():
                if key in str(prof):
                    outfile.write("=====================================================\n")
                    outfile.write(key + " instance:\n")
                    outfile.write("=====================================================\n\n")
                    for line in prof.outbuff:
                        if line == "0":
                            pass
                        else:
                            outfile.write(line + "\n")
                    outfile.write("\n\n")
                    outfile.close()

def save():
    t_score = 0
    t_prof = ''
    t_profraw = profs[0] 
    for prof in profs:
        if prof.score > t_score:
            t_prof = str(prof)
            t_profraw = prof
            t_score = prof.score
    accuracy = t_profraw.getacc()
    for key, val in scores.iteritems():
        if key in t_prof:
            if accuracy > 50:
                scores[key] += 1
                interwrite(t_profraw)
            else:
                scores['unidentified'] += 1

def reset():
    for prof in profs:
        prof.score = 0
        del prof.outbuff[:]

def scan(log):
    reader = csv.reader(log)
    curr_line = '' 
    prev_line = ''
    for line in reader:
        if not line:
            save()
            reset()
            prev_line = ''
            curr_line = ''
        elif line[0] == "process":
            curr_line = '"' + line[2] + '","' + line[3] + '","' + line[4] + '","' + line[5] + '"'
            if line[3] == "created":
                for prof in profs:
                    for proc in prof.procstart:
                        if line[5] == proc:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
            elif line[3] == "terminated":
                for prof in profs:
                    for proc in prof.procterm:
                        if line[5] == proc:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
        elif line[0] == "registry":
            curr_line = '"' + line[2] + '","' + line[3] + '","' + line[4] + '"'
            if line[3] == "SetValueKey":
                for prof in profs:
                    for reg in prof.regset:
                        if line[4] == reg:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
            elif line[3] == "DeleteValueKey":
                for prof in profs:
                    for reg in prof.regdel:
                        if line[4] == reg:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
        elif line[0] == "file":
            curr_line = '"' + line[2] + '","' + line[3] + '","' + line[4] + '"'
            if line[3] == "Write":
                for prof in profs:
                    for f in prof.filewrite:
                        if '.sxx' in line[4]:
                            flashcache.score += 10
                        elif line[4] == f:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
                        else:
                            pass
            elif line[3] == "Delete":
                for prof in profs:
                    for f in prof.filedel:
                        if line[4] == f:
                            if curr_line != prev_line:
                                prof.outbuff.append(curr_line)
                                prev_line = curr_line
                            else:
                                pass
                            prof.score += 1
                
    save()
    reset()
    endwrite()
    print scores

def usage():
    print "Help for hpcscan.py:"
    print "Usage: python hpcscan.py <option> <argument>"
    print "Options include:"
    print "\t-u (--update):\t\t\t\t updates the application from github repo"
    print "\t-f <filename> (--file <filename>):\t specifies the file to be analysed"
    print "\t-h (--help):\t\t\t\t displays this usage dialog"
    
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
            print "Error: Unparsed argument."
            exit(1)

    print "Checking loaded modules...",
    for module in profiles.__all__:
        print module,
    print ""

    scan(log)
    log.close()

profs = []
scores = {}
for module in profiles.__all__:
    exec '%s = profiles.%s.%s()' % (module, module, module)
    exec 'profs.append(%s)' % (module)
    scores[module] = 0
scores['unidentified'] = 0

if __name__ == "__main__":
    main()
