import os
import shutil


def installMods(patch, patch2):
    modsCount = 0
    modsNotInstalled = ''
    for file in os.listdir(patch):
        if file[len(file) - 4:len(file)] == '.brv':
            modsCount += 1
            fileName = file.replace(" ", "_")
            if fileName[:len(fileName)-4] in os.listdir(patch2):
                shutil.rmtree(patch2+"/"+(fileName[:len(fileName)-4]))
                modsNotInstalled += f'{file} '
            os.makedirs(patch2+"/"+(fileName[:len(fileName)-4]))
            shutil.copyfile(f"MetaData.brm", patch2 + "/" + (fileName[:len(fileName) - 4]) + "/MetaData.brm")
            os.rename(patch+"/"+file, patch2+"/"+(fileName[:len(fileName)-4])+"/Vehicle.brv")

            with open(patch2+"/"+(fileName[:len(fileName)-4])+"/MetaData.brm", 'r+') as fh:
                openFile = file[:len(file) - 4]
                if len(openFile) > len("reallylongnamelolxd"):
                    openFile = openFile[:len("reallylongnamelolxd")]
                else:
                    openFile += " "*(len("reallylongnamelolxd") - len(openFile))
                old = fh.read().replace("reallylongnamelolxd", openFile)
                fh.seek(0)
                fh.write(old)
    if modsCount == 0:
        return "NoMods"
    elif modsNotInstalled != '':
        return f"ModsAlredyInstalled{modsNotInstalled}"
    else:
        return "installed"