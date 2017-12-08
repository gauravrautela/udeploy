import requests
from mainfuction2 import *

import json , os, sys, logging, argparse

#Adding parse for argument
parser=argparse.ArgumentParser(description="Create a new GitHub Project")
parser.add_argument('--appName', action='store', required=True)
parser.add_argument('--teamName', action='store', required=True)
parser.add_argument('--configdir', action='store')
parser.add_argument('--user', action='store', required=True)
parser.add_argument('--password', action='store', required=True)

args = parser.parse_args()
appName= args.appName.strip()
teamName = args.teamName.strip()
Username = args.user.strip()
Password = args.password.strip()


ConfigDir="app"
print("App Name =" +appName)
print("Team Name = "+ teamName)

envColor={"Green": "%2317AF4B", "Olive": "%23838329", "Orange": "%23DD731C", "Red": "%23FF0000", "Yellow": "%23FFCF01", "DarkYellow": "%23FDB813", "Purple": "%237F1C7D","BottleGreen": "%23006059", "SeaGreen": "%23008A52", "Teal": "%23007670", "Blue": "%2300B2EF", "MedBlue": "%23008ABF", "DarkBlue": "%2300648D",  "DarkestBlue": "%23003F69", "DarkOlive": "%23594F13", "BrickRed": "%23A91024", "Gray": "%2383827F", "DarkGray": "%23404041" }

ServerEndpoint="http://54.169.134.120:8080"


configcomponent={
    "name": appName,
    "description": "IIB Component",
    "importAutomatically": False,
    "useVfs": True,
    "sourceConfigPlugin": "None",
    "defaultVersionType": "FULL",
}


OUT=create(Username,Password,ServerEndpoint,configcomponent,appName,"/cli/component/create")
print ("Output status" + str(OUT))
if OUT == False:
    print("Failed creating Component "+appName)
 #   sys.exit(100)

configapp={
    "name": appName,
    "description": "IIB Application",
    "enforceCompleteSnapshots": True
}

OUT=create(Username,Password,ServerEndpoint,configapp,appName,"/cli/application/create")
print ("Output status" + str(OUT))
if OUT == False:
    print("Failed creating Application"+appName)
 #   sys.exit(100)

## ADD to team
print ("Adding APP to Team")
toTeam=appToTeam(appName,teamName,ServerEndpoint,Username,Password)

print ("Addning Component to Team")
toTeam=componentToTeam(appName,teamName,ServerEndpoint,Username,Password)

print ("Adding "+appName+" Component to "+appName+" APP")
addComponentToApp(appName,appName,ServerEndpoint,Username,Password)

env={"name": "DEV", "color": envColor["Blue"], "resources": ["First","second"]}

print ("Creating ENV ")
configenv={
    "application" : appName,
    "name" : env["name"],
    "color" : env["color"]
}
OUT=createEnvironment(Username,Password,ServerEndpoint,configenv,appName)
if OUT == False:
    print("Failed creating Enviroment"+appName)

print ("Create Resource")
configresource={
    "name" : appName,
    "role" : appName,
    "parent" : "First"
}
createResource(Username,Password,ServerEndpoint,configresource)

print ("Adding application env to team")
configteam={
    "application" : appName,
    "team" : teamName,
    "environment": env["name"]
}
url = ServerEndpoint+"/cli/environment/teams"
r=requests.put(url,params=configteam,auth=(Username,Password))
print(r.status_code)

print env["name"]
print ("Adding to base  Resource")
configBase={
    "environment" : env["name"],
    "application" : appName,
    "resource" : "Frist"

}
addBaseResourceToEnvironment(Username,Password,ServerEndpoint,configenv)






