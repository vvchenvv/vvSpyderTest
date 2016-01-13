import requests

def SaveLinkIntoFile(links,Prefix,Suffix):
    i = 0
    for each_link in links:
        graphic = requests.get(each_link)
        with open(Prefix+"{0}.".format(i)+Suffix,"wb") as code:
            code.write(graphic.content)
        i = i + 1

#def make_dirs(Targetdir,folder_name):