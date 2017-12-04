from mainfuction import *
import sys


Username=sys.argv[1]
Password=sys.argv[2]
ServerEndpoint=sys.argv[3]
Filename=sys.argv[4]
AppName=sys.argv[5]

print Username
print Password
print Filename
print ServerEndpoint
print AppName

print "Creating Application "+AppName
OUT=createApplication(Username,Password,ServerEndpoint,Filename,AppName)
print "Output status "+ OUT

if OUT == False:
    sys.exit(100)