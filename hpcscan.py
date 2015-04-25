# hpcscan.py
# Author: Aled Rhys Evans <evansar6@cardiff.ac.uk>
# License: Simplified BSD License (FreeBSD License) 
# Description: An utility to look at Capture-HPC logs and determine if a particular set of logs
#              displays malicious actions by comparing it to profiles of logs already determined
#              to be malicious. This is under active development and is not for production use yet. 
import os, sys, subprocess, getopt, profiles, csv

def reset():
    t_score = 0
    t_prof = ''
    t_profraw = 0
    accuracy = 0
    for prof in profs:
        if prof.score > t_score:
#            print "%d larger than %d - replacing" % (prof.score, t_score)
            t_prof = str(prof)
            t_profraw = prof
            t_score = prof.score
            accuracy = t_profraw.getacc()
            prof.score = 0
            del prof.outbuff[:]
    for key, val in scores.iteritems():
        if key in t_prof: 
            if accuracy > 50:
                scores[key] += 1
                accuracy = 0
            else:
                scores['unidentified'] += 1
                accuracy = 0

def scan(log):
    reader = csv.reader(log)
    curr_line = '' 
    prev_line = ''
    for line in reader:
        if not line:
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
                
    reset()
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
