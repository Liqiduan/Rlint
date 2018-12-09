import urllib
import sys,os,posixpath 

class Compiler():
    def __init__(self, server):
        self.server = server

    def normpath(self, path):
        p = path.split(os.sep)
        posix_path = posixpath.sep.join(p)
        return posix_path
    
    def compile(self, filename):
        base = '/home/liqiduan/'
        filename = self.normpath(filename)
        
        args = urllib.urlencode({'base':'/home/liqiduan/', 'file':filename})
        url = self.server + '/compile?' + args
        r = urllib.urlopen(url)
        return r.read()
    
c = Compiler('http://192.168.1.100:5000')
print c.compile(str(sys.argv[1]))


