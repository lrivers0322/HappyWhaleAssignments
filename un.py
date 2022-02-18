import csv
import os.path

import cv2 as cv
import matplotlib.pyplot as plt
csvfile=open('C://Users//ltriv//Downloads//Happy-whale-and-dolphin//train.csv',mode='r')
csvfile=csv.reader(csvfile)
dir='C://Users//ltriv//Downloads//Happy-whale-and-dolphin//train_images'
species=[]
individuals=[]

paths=[]
for i in csvfile:
    species.append(i[1])
    individuals.append(i[2])
    paths.append(i[0])
print(individuals)
speciesCop=[]
for i in species:
    speciesCop.append(i)
indcop=[]
for i in individuals:
    indcop.append(i)
individualsList=[]
q=0
k=0
while q<20:
    if not individuals[k] in individualsList:
        individualsList.append(individuals[k])
        q+=1
    k+=1

specieslist=[]
i=0
m=0
while i<30:
    if not species[m] in specieslist:
        specieslist.append(species[m])
        i+=1
    m+=1
specieslist.remove('species')
#print(individualsList)
#print(individuals)
#print(specieslist)
specindex=[]
for m in range(29):
    for n in range(3):
        print(m)
        specin=species.index(specieslist[m])
        species[specin]='filler'
        specindex.append(specin)
#print(specindex)
#print(individualsList)
indindex=[]
individualsList.remove(('individual_id'))
print(individuals[1])


for i in range(19):
    for n in range(3):
        print(i)
        print(individuals[1])
        if individualsList[i] in individuals:
            indind=individuals.index(individualsList[i])
        else:
            indind=1
        print(indind)

        individuals[indind]='filler'
        indindex.append(indind)
doneind=0
subsplit=3
print(specieslist)

for a in range(subsplit):
    plt.figure(figsize=(20,20))
    plt.subplots_adjust(hspace=.7)
    for n in range(int(20/subsplit)*3):
        plt.subplot(int(20 / subsplit), 3, n + 1)

        plt.xlabel(indcop[indindex[int(n+doneind*(20/subsplit))]])
        plt.ylabel(speciesCop[indindex[int(n+doneind*(20/subsplit))]])
        plt.imshow(cv.cvtColor(cv.imread(os.path.join(dir,paths[indindex[int(n+doneind*(20/subsplit))]])),cv.COLOR_BGR2RGB))
    doneind+=1



done=0
subplotsplit=3
for n in range(subplotsplit):
    plt.figure(figsize=(20, 20))
    plt.subplots_adjust(hspace=.4)
    for i in range(int(30/subplotsplit)*3):
        plt.subplot(int(30/subplotsplit),3,i+1)
        plt.yticks([])
        plt.xlabel(speciesCop[specindex[int(i+done*(30/subplotsplit))]])
        plt.xticks([])
        plt.imshow(cv.cvtColor(cv.imread(os.path.join(dir,paths[specindex[int(i+done*(30/subplotsplit))]])),cv.COLOR_BGR2RGB))
    done+=1
plt.show()
print(individualsList)


