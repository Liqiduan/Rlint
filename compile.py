import urllib,urllib2
import sys,os,posixpath 

class Compiler():
    def __init__(self, url):
        self.url = url

    def normpath(self, path):
        p = path.split(os.sep)
        posix_path = posixpath.sep.join(p)
        return posix_path
    
    def compile(self, filename):
        filename = self.normpath(filename)
        
        with open(filename, 'rb') as f:
            s = f.read()

        arg = {'file':s, 'fname':filename, 'base':'/home/liqiduan'}
        conn = urllib2.urlopen(self.url, data=urllib.urlencode(arg)) 

        return conn.read()
    
c = Compiler('http://192.168.1.100:5000/compile')
print c.compile(str(sys.argv[1]))


