
import os

zCompletListFiles = []
originPath = 'REPERTOIRE'
diagfile = open('autoDaig2.mmd','w')


#init mermaid class diagram
def initMermaid():
    diagfile.write('classDiagram \n')


#recupere les noms des modules/directories
def initRepo():
    zNameDir = os.listdir(originPath)
    for i in range(len(zNameDir)):
        diagfile.write('Program --> ' + zNameDir[i] + '\n')

#recupere les path de tout les fichiers du repertoire original
def pathList(racine,i):
            nameFile = os.path.join(racine, i)
            # diagfile.write(nameFile + '\n')
            zCompletListFiles.append(nameFile)



def main():
    initMermaid()
    for root, dirs, files in os.walk(originPath):        
        for i in files:
            pathList(root,i)
    
    reposplit = zCompletListFiles[1].split('\\')
    initRepo()





main()

print(zCompletListFiles[1])
test = zCompletListFiles[29].split('\\') #Files[nb] -> nb = lines 
print (test[1]) #[nb] -> nb parameters in the line
        




    


