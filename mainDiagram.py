import os

TAILLE_TRAITEMENT = 47 #BMT Supp
PATH = 'REPERTOIRE'
PATH_MERMAID = 'Class_Diagram.mmd'

# Main
def main():
    zMermaidFile = open(PATH_MERMAID,'w')
    zCompletListFiles = []
    zNbFiles=0

    # Init mermaid class diagram
    zMermaidFile.write('classDiagram \n')

    # List all the path
    for root, dirs, files in os.walk(PATH):        
        for i in files:
            nameFile = os.path.join(root, i)
            #zMermaidFile.write(nameFile + '\n')
            zCompletListFiles.append(nameFile)
            zNbFiles = zNbFiles + 1
    print(zNbFiles)#BMT Supp


    # Generate links
    for i in range(TAILLE_TRAITEMENT):
        splitText = zCompletListFiles[i].split('\\')
        
        # Writing Modules Links of the Programm
        module = splitText[1]
        zMermaidFile.write('Modules --> ' + module + '\n')
        
        # Writing files links with theyre modules
        maxLenList = len(splitText)
        fichier = splitText[maxLenList - 1]
        fichierCourt = fichier.split('.')

        zMermaidFile.write(module + ' --> ' + fichierCourt[0] + '\n')

        # Writing includes in the files
        includeWord = 'include '
        fileCheck = open(zCompletListFiles[i],'r')
        for line in fileCheck:
            if includeWord in line:
                if '/*' in line:
                    cleanInclude = line.split('/*')
                else:
                    cleanInclude = line.split('//')
                cleanInclude[0] = line.replace('-','_')
                
                zMermaidFile.write(fichierCourt[0] + ' : ' + cleanInclude[0] + '\n') 
        fileCheck.close()
            
    # Writing functions in the files
            #print(zCompletListFiles[i])

        
#######################################################

# clean Links doublons
def cleanFileLinks():
        
    ls = []
    MermaidFile = PATH_MERMAID

    with open(MermaidFile, 'r') as file:

        for line in file:

            if line not in ls:
                ls.append(line)

    with open(MermaidFile, 'w') as file:
        for line in ls:
            file.write(line)


######################################################


main()
cleanFileLinks()

