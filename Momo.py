from flask import Flask
import sys
import csv


app= Flask(__name__)


class Personne:
    _id = 0
    _nom =""
    _solde =" "

    def __init__(self, nom,solde):
        self._id +=1
        self._nom = nom
        self._solde = solde

    def getId(self):
        return self._id

    def getNom(self):
        return self._nom

    def getSolde(self):
        return self._solde

    def setSolde(self,montant):
        self._solde= self._solde + montant

Personnes=[]
listTransaction=[]
increment= 4

@app.route("/")
def afficherClient():
    affiche = "<h3>Liste de Personne :</h3>\n"
    for personne in range(len(Personnes)):
       	affiche += "<p>" + personne.toString() + "</p>\n"
    return affiche

@app.route("/addCompte/<string:nom>/<float:solde>")
def addCompte(Nom, solde):
    for i in range(len(Personnes)):
        if (Personnes[i].getNom()==Nom):
            return "Un client avec les meme nom est deja dans la banque"

    client=Personne(Nom,solde)
    Personnes.append(client)
    print("le client a été ajouté a la banque")
    return client


def checktransaction(P1,transac):
    if (P1.getSolde() < transac) :
        return False
    return True


@app.route("/addTransaction/<int:id1>/<int:id2>/<float:transfert>")
def addTransaction(id1,id2,transfert):
    trans=[id1,id2,transfert]
    if (checktransaction(Personnes[id1], transfert) == True) :
        Personnes[id1].setSolde(transfert)
        Personnes[id2].setSolde(-transfert)
        listTransaction.append(trans)
        return "La transaction d'un montant de:", transfert, "entre ", Personnes[id1].getNom(), " et ", Personnes[id2].getNom(), "à été effectué"
    return Personnes[id1], "ne peut pas transferer", transfert, "car son solde est trop faible"

@app.route("/afficherTransaction/")
def afficherTransaction():
    List = trie(listTransaction)	
    for i in range(len(List)):
        print(List[i])


def trie(L):
    return sorted(L, key=lambda L: L[2])

@app.route("/afficherTransactionPersonne/<int:id>")
def afficherTransactionPersonne(id):
	List = trie(listTransaction)
    	for i in range(len(List)):
        if(List[0] == id) || (List[1] == id):	
		print(List[i])

@app.route("/printSolde/<int:id>")		
def printSold(id):
	for i in range(len(Personnes):
		if (Personnes[i].getId()==id):
			return ("Le solde du compte est: ", Personnes[i].getsolde(),"euros")
	
	
	
addCompte("Max", 10)
addCompte("Benjamin",1000)
addCompte("Baptiste",0)


#afficherClient()


addTransaction(1,0,100)
addTransaction(1,2,10)
#afficherTransaction()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)
