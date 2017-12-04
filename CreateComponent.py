from mainfuction import *
import sys


Username=sys.argv[1]
Password=sys.argv[2]
Filename=sys.argv[3]
ComponentName=sys.argv[4]

print Username
print Password
print Filename
print ComponentName
print "Creating Component "+ComponentName
print createComponent(Username,Password,Filename,ComponentName)