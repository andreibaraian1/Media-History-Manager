import os
import easygui
import json
import subprocess

mediaPlayerPath = "Your path to media player "

def startUpdateMedia(property,media):
    for item in media:
        if item["path"] == property["path"]:
            item["status"]='OPENED'
            break
    else:
        item = None
    if(item):
        createFile=open(f"{path}/config.txt","w")
        createFile.write(json.dumps(media))
        createFile.close()

def getConfig(path):
    media = []
    for file in os.listdir(path):
        if file.endswith((".mkv",".mp4")):
             media.append({"path":file, "status": "NOT_OPENED"})
        if(not os.path.exists(f"{path}/config.txt")):
            createFile=open(f"{path}/config.txt","w")
            createFile.write(json.dumps(media))
            createFile.close()
        readFile=open(f"{path}/config.txt","r")
        prevMedia = json.loads(readFile.read())
    list_names = [value for item in prevMedia for value in item.values()]
    for item in media:
        if(item["path"] not in list_names):
            prevMedia.append(item)
            createFile=open(f"{path}/config.txt","w")
            createFile.write(json.dumps(media))
            createFile.close()
    return prevMedia

path=easygui.diropenbox(msg="Choose a file")
files = os.listdir(path)
media = getConfig(path)
msg="Select the media to play"
choices = []
for item in media:
    status=item["status"]
    name=item["path"]
    choices.append(f"Status : {status} Name:{name}")

reply=easygui.choicebox(msg,choices=choices)
name = (reply.split("Name:",1)[1])
findDict = next((item for item in media if item["path"] == name), None)
print(findDict)
startUpdateMedia(findDict,media)
file = findDict["path"]
subprocess.Popen([mediaPlayerPath,f"{path}/{file}"])

