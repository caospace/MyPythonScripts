import os

if __name__ == "__main__":
    if os.name == "nt":
        print "You are using %s." % os.environ['COMPUTERNAME']
    elif os.name == "posix":
        host = os.popen("echo $HOSTNAME")
        try:
            hostname = host.read()
            print "You are using %s." % hostname
        finally:
            host.close()
    else:
        print "Unknown system."
