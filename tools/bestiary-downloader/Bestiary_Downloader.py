import os
import urllib.request as ul
from urllib.request import *
import re

url = "https://www.emberwindgame.com/bestiary/"
site = ul.urlopen(url)

artless = ""
while artless.lower() != "y" and artless.lower() != "n":
    artless = input("Include artless pdfs? (Y/N) ")
    
foes = re.findall("https://.*pdf", site.read().decode("utf8"))

if artless.lower() == "n":
    foes = [foe for foe in foes if "artless" not in foe]

if not os.path.exists("Foes"):
    os.mkdir("Foes")

newFoes = []
 
for foe in foes:
    name = foe.replace("https://www.emberwindgame.com/wp-content/uploads/Emberwind_","")
    if not os.path.exists("Foes/"+name):
        newFoes.append(foe)

for foe in newFoes:
    name = foe.replace("https://www.emberwindgame.com/wp-content/uploads/Emberwind_","")
    if not os.path.exists("Foes/"+name):
        print("["+str((newFoes.index(foe)+1))+"/"+str(len(newFoes))+"] Downloading "+name.replace(".pdf","")+" to "+os.path.abspath("Foes/"+name))
        ul.urlretrieve(foe, "Foes/"+name)

site.close()

print("Finished!")

input()
