from mainfuction import *
import sys


Username=sys.argv[0]
Password=sys.argv[1]
Filename=sys.argv[2]
ComponentName=sys.argv[3]

print "Creating Component "+ComponentName
print createComponent(Username,Password,Filename,ComponentName)