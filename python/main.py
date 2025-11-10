import os

path = "../img/Articles/Mondial_de_l_auto_Paris_2024/"
exept = "redimentionné_compressé_SD.jpg"
rename = "resized_compressed_SD.jpg"

def inspectfile(file, pathfile):
    if file == exept:
        print("RENAMED >>> " + pathfile + file)
        os.rename(pathfile + file, pathfile + rename)
    elif file == rename:
        print("ALREADY RENAMED >>> " + pathfile + file)
    else:
        print("DELETED >>> " + pathfile + file)
        os.remove(pathfile + file)


while True:
    for i in os.listdir(path):
        if "." in i:
            inspectfile(i, path)
        else:
            for j in os.listdir(path + i + "/"):
                if "." in j:
                    inspectfile(j, path + i + "/")
                else :
                    for k in os.listdir(path + i + "/" + j + "/"):
                        if "." in k:
                            inspectfile(k, path + i + "/" + j + "/")
                        else:
                            for l in os.listdir(path + i + "/" + j + "/" + k + "/"):
                                if "." in l:
                                    inspectfile(l, path + i + "/" + j + "/" + k + "/")
                                else:
                                    for n in os.listdir(path + i + "/" + j + "/" + k + "/" + l + "/"):
                                        if "." in n:
                                            inspectfile(n, path + i + "/" + j + "/" + k + "/" + l + "/")
                                        else:
                                            print("FOLDER >>> " + path + i + "/" + j + "/" + k + "/" + l + "/")
    break