from os import path

#--------------------------------------------

try:
    exec(open("config.cfg", "r").read())
except:
    error = True

if error:
    file = open("config.cfg", "w")
    file.write("cryengineDirectory = \"D:/Cryengine/GameSDK\"")
    file.close()

    exec(open("config.cfg", "r").read())
