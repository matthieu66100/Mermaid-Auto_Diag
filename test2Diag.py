import os

# Main
def main():
    zCompletListFiles = []
    originPath = 'REPERTOIRE'
    diagfile = open('autoDaig2.mmd','w')


    # Init mermaid class diagram
    diagfile.write('classDiagram \n')

    # List all the path
    for root, dirs, files in os.walk(originPath):        
        for i in files:
            nameFile = os.path.join(root, i)
            #diagfile.write(nameFile + '\n')
            zCompletListFiles.append(nameFile)


    # Generate links
    for i in range(10):
        splitText = zCompletListFiles[i].split('\\')
        
        # Writing Modules Links of the Programm
        module = splitText[1]
        diagfile.write('Modules --> ' + module + '\n')
        
        # Writing files links with theyre modules
        maxLenList = len(splitText)
        fichier = splitText[maxLenList - 1]
        fichiercourt = fichier.split('.')

        diagfile.write(module + ' --> ' + fichiercourt[0] + '\n')

        # Writing includes in the files
        includeWord = 'include'
        fileCheck = open(zCompletListFiles[i],'r')
        for line in fileCheck:
            if includeWord in line:
                diagfile.write(module + ' : ' + line + '\n')

            
    # Writing functions in the files
            #print(zCompletListFiles[i])

        
#######################################################

# clean Links doublons
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


main()
cleanFileLinks()

