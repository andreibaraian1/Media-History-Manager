import os
import vlc
import easygui
import json
import ast

def startUpdateMedia(property,media):
    result = ast.literal_eval(property)
    for item in media:
        if item["path"] == result["path"]:
            item["status"]='STARTED'
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
             media.append({"path":file, "status": "NOT_STARTED"})
        if(not os.path.exists(f"{path}/config.txt")):
            createFile=open(f"{path}/config.txt","w")
            createFile.write(json.dumps(media))
            createFile.close()
        readFile=open(f"{path}/config.txt","r")
        prevMedia = json.loads(readFile.read())
    for item in media:
        if(item not in prevMedia):
            prevMedia.append(item)
            createFile=open(f"{path}/config.txt","w")
            createFile.write(json.dumps(media))
            createFile.close()
    return prevMedia

path=easygui.diropenbox(msg="Choose a file")
files = os.listdir(path)
media = getConfig(path)
msg="Select the media to play"
reply=easygui.choicebox(msg,choices=media)
startUpdateMedia(reply,media)



# media_player = vlc.MediaPlayer()
  

# media = vlc.Media("test.mkv")
  

# media_player.set_media(media)
  

# media_player.play()
