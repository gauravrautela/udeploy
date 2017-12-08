import requests
import json


def create(User,Password,ServerEndpoint,config,componentName,url):
    print ("Creating component"+componentName)
    CreateComponentUri=url
    headers = {
        'Accept': 'application/json'
               }
    CreateUrl= ServerEndpoint+CreateComponentUri
    print "Url - "+CreateUrl+User+Password
    request_create = requests.put(CreateUrl,headers=headers,data=json.dumps(config),auth=(User,Password))
#    request_create = requests.put(CreateUrl,data=json.dumps(config),headers=headersID)
    if request_create.status_code != 200:
       print ("Component create request failed " + request_create.content)
       return False
    print ("Request Passed - Returning Response content")
    print json.loads(request_create.content)
    return json.loads(request_create.content)



def createComponent(User,Password,ServerEndpoint,config,componentName):
    print ("Creating component"+componentName)
    CreateComponentUri="/cli/component/create"
    headers = {'Accept': 'application/json'}
    CreateUrl= ServerEndpoint+CreateComponentUri
    print "Url - "+CreateUrl
    request_create = requests.put(CreateUrl, headers=headers,data=json.dumps(config),auth=(User,Password))
    if request_create.status_code != 200:
       print ("Component create request failed " + request_create.content)
       return False
    print ("Request Passed - Returning Response content")
    print json.loads(request_create.content)
    return json.loads(request_create.content)




def getAppInfo(AppName):
    AppInfoUri="/cli/application/info"
    AppInfoUrl=ServerEndpoint+AppInfoUri
    payload = {"application" : AppName}
    requestAppInfo=requests.get(AppInfoUrl,params=payload,auth=(User,Password))
    if requestAppInfo.status_code != 200:
        print "Request Failed - getAppInfo " + requestAppInfo.content
        return False
    print "Request Passed - Returning Response content"
    print json.loads(requestAppInfo.content)
    return json.loads(requestAppInfo.content)


def createApplication(User,Password,ServerEndpoint,configDir,AppName):
    print "Creating Application - "+AppName
    createApplicationUri="/cli/application/create"
    createApplicationUrl=ServerEndpoint+createApplicationUri
    FilePath = configDir + "/application.json"
    json_data = open(FilePath)
    headers = {'Accept': 'application/json'}
    requestAppCreate= requests.put(createApplicationUrl, headers=headers,data=json_data,auth=(User,Password))
    if requestAppCreate.status_code != 200:
       print "App create request failed" + requestAppCreate.content
       return False
    print "Request Passed - Returning Response content"
    print json.loads(requestAppCreate.content)
    return json.loads(requestAppCreate.content)

def addComponentToApp(componentName,appName,ServerEndpoint,Username,Password):
    print "Adding "+componentName+" to app "+appName
    addComponentToAppUri="/cli/application/addComponentToApp"
    addComponentToAppUrl=ServerEndpoint+addComponentToAppUri
    payload = {
        "component" : componentName,
        "application" : appName
    }
    requestAddComponentToApp=requests.put(addComponentToAppUrl,params=payload,auth=(Username,Password))
    if requestAddComponentToApp.status_code != 200:
        print "Component add to App request failed" + requestAddComponentToApp.content
        return False
    print "Request Passed - Returning Response content"
    print json.loads(requestAddComponentToApp.content)
    #return json.loads(requestAddComponentToApp.content)
    return True


def createEnvironment(Username,Password,ServerEndpoint,configenv,appName):
    print "Creating Enviroment for "+appName
    createEnvUri="/cli/environment/createEnvironment"
    createEnvUrl=ServerEndpoint+createEnvUri
    requestCreateEnv=requests.put(createEnvUrl,params=configenv,auth=(Username,Password))
    if requestCreateEnv.status_code != 200:
        print "Create Enviroment to App request failed" + requestCreateEnv.content
        return False
    print "Request Passed - Returning Response content"
    print requestCreateEnv.content
    return requestCreateEnv.content

def addTagToApplication(tag,appName):
    print "Add Tag "+tag+" to "+ appName
    addTagToApplicationUri="/cli/application/tag"
    addTagToApplicationUrl=ServerEndpoint+addTagToApplicationUri
    payload={
        "application" : appName,
        "tag" : tag
    }
    requestAddTagToApplication=request.put(addTagToApplicationUrl,params=payload,auth=(User,Password))
    if requestAddTagToApplication.status_code != 200:
        print "Adding tag Failed "+ requestAddTagToApplication.content
        return False
    print "Adding Tag to App Passed"
    return True

def appToTeam(appName,teamName,ServerEndpoint,User,Password):
    print "Adding app "+appName+" to "+teamName
    appToTeamUri="/cli/application/teams"
    appToTeamUrl=ServerEndpoint+appToTeamUri
    payload = {
        "application" : appName,
        "team" : teamName
    }
    requestAppToTeam=requests.put(appToTeamUrl,params=payload,auth=(User,Password))
    if requestAppToTeam.status_code != 200:
        print "Add app to Team Failed"
        return False
    print "Adding "+appName+" to "+teamName
    return True

def componentToTeam(componentName,teamApp,ServerEndpoint,User,Password):
    print "Adding component "+componentName+" to "+teamApp
    componentToTeamUri="/cli/component/teams"
    componentToTeamUrl=ServerEndpoint+componentToTeamUri
    payload = {
        "component" : componentName,
        "team" : teamApp
    }
    requestComponentToTeam=requests.put(componentToTeamUrl,params=payload,auth=(User,Password))
    if requestComponentToTeam.status_code != 200:
        print "Adding Component to Team Failed"
        return False
    print "Adding "+componentName+" to "+teamApp
    return True

def getResourceInfo(resourceId):   #provide resource ID
    print "Checking "+resourceId+" info"
    getResourceExisUri="/cli/resource/info"
    getResourceExisUrl=ServerEndpoint+getResourceExisUri
    payload = {
        "resource" : resourceId
    }
    requestgetResourceInfo=requests.get(getResourceExisUrl,params=payload,auth=(User,Password))
    if requestgetResourceInfo.status_code != 200:
        print "Info for Resource Failed"
        return False
    print "Resource Info Check Passed for "+resourceId
    return json.loads(requestgetResourceInfo.content)

def getComponentInfo(componentId):
    print "Checking "+componentId+" Info"
    getComponentInfoUri="/cli/component/info"
    getComponentInfoUrl=ServerEndpoint+getComponentInfoUri
    payload = {
        "component" : componentId
    }
    requestGetComponentInfo=requests.get(getComponentInfoUrl,params=payload,auth=(User,Password))
    if requestGetComponentInfo.status_code != 200:
        print "Component info check Failed"
        return False
    print "Component Info Check Passed for "+componentId
    print "Response Payload"+requestGetComponentInfo.content
    return json.loads(requestGetComponentInfo.content)

def getEnvInfo(envId,appName=None):  # Application name is required if Env Id is not provided
    print "Checking "+envId+" Info"
    getEnvInfoUri="/cli/environment/info"
    getEnvInfoUrl=ServerEndpoint+getEnvInfoUri
    payload = {
        "environment" : envId
    }
    requestGetEnvInfo=requests.get(getEnvInfoUrl,params=payload,auth=(User,Password))
    if requestGetEnvInfo.status_code != 200:
        print "Get Env Info Failed for "+envId
        return False
    print "Get Env Info passed for "+envId
    return json.loads(requestGetEnvInfo.content)

def getAppProcessInfo(appName,processName):
    print "Get info for process "+processName+" of app "+appName
    getAppInfoUri="/cli/applicationProcess/info"
    getAppInfoUrl=ServerEndpoint+getAppInfoUri
    payload = {
        "application" : appName,
        "applicationProcess" : processName
    }
    requestGetAppProcessInfo=requests.get(getAppInfoUrl,params=payload,auth=(User,Password))
    if requestGetAppProcessInfo.status_code != 200:
        print "Get App process info failed"
        return False
    print "Get App process Info Passed"
    return  json.loads(requestGetAppProcessInfo.content)

def createResource(Username,Password,ServerEndpoint,json_data):
    print "Creating Resouce "
    createResourceUri="/cli/resource/create"
    createResourceUrl=ServerEndpoint+createResourceUri
    headers = {'Accept': 'application/json'}
    requestCreateResource = requests.put(createResourceUrl, headers=headers, data=json.dumps(json_data), auth=(Username, Password))
    if requestCreateResource.status_code != 200:
        print "Creating Resouce  failed"
        print requestCreateResource.content
        return False
    print "Created resource "
    print requestCreateResource.content
    return json.loads(requestCreateResource.content)

def addBaseResourceToEnvironment(Username,Password,ServerEndpoint,payload):
    print "Adding base resource to Environment"
    addBaseResourceToEnviromentUri="/cli/environment/addBaseResource"
    addBaseResourceToEnviromentUrl=ServerEndpoint+addBaseResourceToEnviromentUri
    requestAddBaseResourceToEnvironment=requests.put(addBaseResourceToEnviromentUrl,params=payload,auth=(Username,Password))
    if requestAddBaseResourceToEnvironment.status_code != 200:
        print "Add Base Resource to Enviroment Failed"
        print requestAddBaseResourceToEnvironment.content
        return False
    print "Added Resouce "+resourceId+ " to Environment "
    print requestAddBaseResourceToEnvironment.content
    return True

def createApplicationProcess(appProcessname,fileName):
    print "Creating App process "+appProcessname
    createApplicationProcessUri="/createApplicationProcess"
    createApplicationProcessUrl=ServerEndpoint+createApplicationProcessUri
    FilePath = ConfigDir + "/" + fileName
    json_data = open(FilePath)
    headers = {'Accept': 'application/json'}
    requestCreateAppProcess = requests.put(createApplicationProcessUrl,headers=headers, data=json_data, auth=(User, Password))
    if requestCreateAppProcess.status_code != 200:
        print "Creating App Process Failed "+appProcessname
        print requestCreateAppProcess.content
        return False
    print "Created App Process "+appProcessname
    print requestCreateAppProcess.content
    return json.loads(requestCreateAppProcess.content)



def createComponentProcess(componentProcessFileName,componentProcessName):
    print "Creating component Process "+componentProcessName
    createComponentProcessUri="/cli/componentProcess/create"
    createComponentProcessUrl=ServerEndpoint+createComponentProcessUri
    FilePath = ConfigDir + "/" + componentProcessFileName
    json_data = open(FilePath)
    headers = {'Accept': 'application/json'}
    requestComponentProcess= requests.put(createComponentProcessUrl,headers=headers, data=json_data, auth=(User, Password))
    if requestComponentProcess != 200:
        print "Creating component process Failed" +componentProcessName
        print requestComponentProcess.content
        return False
    print "Created Component Process" + componentProcessName
    print requestComponentProcess.content
    return json.loads(requestComponentProcess.content)







######################
def getComponentInfo2(ComponentName):
    print "Getting Component Info for component name " + ComponentName
    ComponentInfoUri="/cli/component/info"
    ComponentInfoUrl=ServerEndpoint+ComponentInfoUri
    payload = {"component" : ComponentName}
    requestComponentInfo=requests.get(ComponentInfoUrl,params=payload,auth=(User,Password))
    if requestComponentInfo.status_code != 200:
        print "Request Failed - getComponentInfo " + requestComponentInfo.content
        return False
    print "Request Passed - Returning Response content"
    print json.loads(requestComponentInfo.content)
    return json.loads(requestComponentInfo.content)
