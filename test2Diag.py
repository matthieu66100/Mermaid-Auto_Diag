
import os

zCompletListFiles = []
originPath = 'REPERTOIRE'
diagfile = open('autoDaig2.mmd','w')


#init mermaid class diagram
diagfile.write('classDiagram \n')


#recupere les noms des modules/directories
zNameDir = os.listdir(originPath)
for i in range(len(zNameDir)):
    diagfile.write('Program --> ' + zNameDir[i] + '\n')

#recupere les path de tout les fichiers du repertoire original
for root, dirs, files in os.walk(originPath):        
    for i in files:
        nameFile = os.path.join(root, i)
        diagfile.write(nameFile + '\n')
        zCompletListFiles.append(nameFile)


        




    


