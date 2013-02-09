import urllib2, httplib, os, sys, pyRedirector

# Banner
def Banner():
    print("=================================================")
    print("pyLongURL v0.1                                   ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <short_URL>\n") % (cmd)
    print("Please enter need an URL!")
    
def main(szURL):
    httplib.HTTPConnection.debuglevel = 1
    request = urllib2.Request(szURL)
    opener = urllib2.build_opener(pyRedirector.RedirectHandler())
    f = opener.open(request)
    print("Shortened url: %s - Long url:%s\n" %(szURL, f.url))
    
if __name__ == "__main__":
    Banner()
    if len(sys.argv)<2:
        help_menu(sys.argv[0])
    else:
        main(sys.argv[1])