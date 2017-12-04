from mainfuction import *
import sys


Username=sys.argv[1]
Password=sys.argv[2]
ServerEndpoint=sys.argv[3]
Filename=sys.argv[4]
ComponentName=sys.argv[5]

print Username
print Password
print Filename
print ServerEndpoint
print ComponentName

print "Creating Component "+ComponentName
OUT=createComponent(Username,Password,ServerEndpoint,Filename,ComponentName)

if OUT == "False":
    sys.exit(100)
