import json

"""
file : Correspont a l'emplacement du fichier JSON
Flag : Correspont a quelle est l'emplacement de la valeur que vous voulez modifier ou lire
valeur :  correspont a la valeur que vous voulez modifer
vardict : Correspont au nom du dictionnaire que vous voulez rajouter
newDictName : corespont au dictionnaire que vous voulez rajouter   
"""
class jsonWork : 
    def __init__(self,file):
        self.fichier = file
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)
    
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict,writeFile,indent=2)  
         
    def lectureSimpleJSON(self):#Permet de juste recuperer le contenu d'un fichier JSON
        with open(self.fichier, 'r') as openfile:
            dictionnaire = json.load(openfile)
        return dict(dictionnaire)
    