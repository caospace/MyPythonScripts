import os
import time

ISOTIMEFORMAT = "%Y-%m-%d %X"

if __name__ == "__main__":
    print "Current directory is %s." % os.getcwd()
    print "Current time is %s." % time.strftime(ISOTIMEFORMAT, time.localtime())
    print "Current time is %s." % time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    print "Current global time is %s." % time.strftime(ISOTIMEFORMAT, time.gmtime(time.time()))
    print "Current time is %s." % time.ctime()
