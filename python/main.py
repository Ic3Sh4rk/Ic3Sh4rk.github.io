from os import rename, remove, listdir
from time import sleep

path = "../img/Portefolio/"
exept_filename = ["redimentionné_compressé_SD.jpg", "redimentionné_compressé_SD.png"]
rename_filename = ["resized_compressed_SD.jpg", "resized_compressed_SD.png"]
test = True

def inspectfile(file, pathfile):
    if file == exept_filename[0]:
        if not test:
            rename(pathfile + file, pathfile + rename_filename[0])
        print("RENAMED >>> " + pathfile + file)
    elif file == exept_filename[1]:
        if not test:
            rename(pathfile + file, pathfile + rename_filename[1])
        print("RENAMED >>> " + pathfile + file)
    elif file == rename:
        print("ALREADY RENAMED >>> " + pathfile + file)
    else:
        if not test:
            remove(pathfile + file)
        print("DELETED >>> " + pathfile + file)

reply = input("Test ? (Y/N) >>> ")
if reply == "N" or reply == "n":
    for i in range(6):
        print("DELETE MODE in " + str(5-i))
        sleep(1)
    test = False


while True:
    for i in listdir(path):
        if "." in i:
            inspectfile(i, path)
        else:
            for j in listdir(path + i + "/"):
                if "." in j:
                    inspectfile(j, path + i + "/")
                else :
                    for k in listdir(path + i + "/" + j + "/"):
                        if "." in k:
                            inspectfile(k, path + i + "/" + j + "/")
                        else:
                            for l in listdir(path + i + "/" + j + "/" + k + "/"):
                                if "." in l:
                                    inspectfile(l, path + i + "/" + j + "/" + k + "/")
                                else:
                                    for n in listdir(path + i + "/" + j + "/" + k + "/" + l + "/"):
                                        if "." in n:
                                            inspectfile(n, path + i + "/" + j + "/" + k + "/" + l + "/")
                                        else:
                                            print("FOLDER >>> " + path + i + "/" + j + "/" + k + "/" + l + "/")
    break