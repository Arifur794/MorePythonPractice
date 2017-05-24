# version 3:  log file name is now a command line argument.
#             You may hard code the name "log" if you prefer. See last comment
#              of file.

import sys             # version 3
import subprocess
import re

# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR( ):
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
#
def log2hist(logfilename):
    # fill in your code here
d = {}
    with open(logfilename, 'r') as f:
        for line in f.readlines():
            words = line.split()
            if 'user:' in words:
                user = words[words.index('user:')+1]
                pages = int(words[words.index('pages:')+1])
                d[user] = d.setdefault(user, 0) + pages
    with open('data', 'w') as f:
        for pages in d.itervalues():
            f.write("%d\n" % pages)
    return runR()
    

if __name__ == '__main__':
    log2hist(sys.argv[1])  # version 2.

# line above may be changed to log2hist("log")

