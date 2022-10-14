import os

def main():
    zCompletListFiles = []
    originPath = 'REPERTOIRE'
    diagfile = open('autoDaig2.mmd','w')


    #init mermaid class diagram
    diagfile.write('classDiagram \n')

    #main
    for root, dirs, files in os.walk(originPath):        
        for i in files:
            nameFile = os.path.join(root, i)
            # diagfile.write(nameFile + '\n')
            zCompletListFiles.append(nameFile)


    #generate links
    for i in range(40):
        splitText = zCompletListFiles[i].split('\\')
        
        module = splitText[1]
        
        maxLenList = len(splitText)
        fichier = splitText[maxLenList - 1]
        fichiercourt = fichier.split('.')

        diagfile.write('test --> ' + module + '\n')
        diagfile.write(module + ' --> ' + fichiercourt[0] + '\n')
        
#clean Links doublons

def cleanFileLinks():
        
    ls = []
    filename = 'autoDaig2.mmd'
    
    

    with open(filename, 'r') as file:

        for line in file:

            if line not in ls:
                ls.append(line)


    with open(filename, 'w') as file:
        for line in ls:
            file.write(line)


######################################################



cleanFileLinks()